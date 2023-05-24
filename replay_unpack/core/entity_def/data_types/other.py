# coding=utf-8
import logging
import socket
import struct
from collections import OrderedDict
from io import BytesIO
from struct import unpack
from typing import Iterable, Dict, Tuple

from lxml import etree

from .base import DataType
from .constants import INFINITY
from .nested_types import PyFixedDict, PyFixedList
from .numeric import UInt8, UInt16


class _DataType(DataType):

    def _get_value_from_stream(self, stream: BytesIO, header_size):
        raise NotImplementedError

    def _get_default_value_from_section(self, section: etree.ElementBase):
        raise RuntimeError("_get_default_value_from_section for "
                           "%s is not defined, value: %s" % (self.__class__.__name__, section))


class Blob(_DataType):
    """
    BLOB
    — Size (bytes): N+k
    Binary data. Similar to a string, but can contain NULL characters.
    Stored in base-64 encoding when in XML, e.g., in the XML database.
    N is the number of bytes in the blob, and k=4.
    """
    _DATA_SIZE = INFINITY

    def _get_size_from_stream(self, stream):
        size, = unpack('B', stream.read(1))

        if size == 0xff:
            data_0, data_1, data_2 = unpack('BBB', stream.read(3))
            # dirty magic of packing integer in 3 bytes
            # https://github.com/Monstrofil/bigworld-2.0/blob/5969290b3f1710910c7cecdad6a34b2016fad9e7/lib/cstdmf/binary_stream.hpp#L265
            # https://github.com/Monstrofil/bigworld-2.0/blob/5969290b3f1710910c7cecdad6a34b2016fad9e7/lib/cstdmf/binary_stream.ipp#L162
            size = (data_2 << 16) | (data_1 << 8) | data_0
            return size
        return size

    def _get_value_from_stream(self, stream: BytesIO, header_size: int):
        size = self._get_size_from_stream(stream)

        payload = stream.read(size)

        assert len(payload) == size, "Expected: %s, size: %s" % (size, len(payload))

        return payload

    def _add_value_to_stream(self, stream: BytesIO, payload: bytes, header_size: int):
        if len(payload) < 0xff:
            UInt8().write_to_stream(stream, len(payload))
        else:
            UInt8().write_to_stream(stream, 0xff)
            UInt16().write_to_stream(stream, len(payload))
            # TODO: actually this is 3'd byte of len, but who cares?
            UInt8().write_to_stream(stream, 0x00)

        stream.write(payload)


class String(_DataType):
    """
    STRING
    — Size (bytes): N+k
    Binary string data.
    """

    _DATA_SIZE = INFINITY
    DEFAULT_VALUE = ''

    def _get_value_from_stream(self, stream: BytesIO, header_size: int):
        size, = unpack('B', stream.read(1))
        # hack for arenaStateReceived
        if size == 0xff:
            size, = unpack('H', stream.read(2))
            # some dummy shit
            unpack('B', stream.read(1))

            _str = stream.read(size)
        else:
            _str = stream.read(size)
        try:
            return _str.decode('utf-8')
        except UnicodeDecodeError:
            # probably this is a pickle string or smtg like that
            return _str

    def _add_value_to_stream(self, stream: BytesIO, payload: str, header_size: int):
        if len(payload) < 0xff:
            UInt8().write_to_stream(stream, len(payload))
        else:
            UInt8().write_to_stream(stream, 0xff)
            UInt16().write_to_stream(stream, len(payload))
            # TODO: actually this is 3'd byte of len, but who cares?
            UInt8().write_to_stream(stream, 0x00)

        if not isinstance(payload, bytes):
            stream.write(payload.encode('utf-8'))
        else:
            stream.write(payload)

    def _get_default_value_from_section(self, section: etree.ElementBase):
        assert isinstance(section.text, str)
        return section.text


class Python(_DataType):
    """
    BLOB
    — Size (bytes): N+k
    Binary data. Similar to a string, but can contain NULL characters.
    Stored in base-64 encoding when in XML, e.g., in the XML database.
    N is the number of bytes in the blob, and k=4.
    """

    _DATA_SIZE = INFINITY

    def _get_value_from_stream(self, stream: BytesIO, header_size: int):
        size, = unpack('B', stream.read(1))
        return stream.read(size)


class FixedDict(_DataType):

    def __init__(self, attributes: Dict[str, DataType], allow_none=False, header_size=1):
        self.allow_none = allow_none
        self.attributes = attributes  # type: OrderedDict
        super(FixedDict, self).__init__(header_size=header_size)

    def _get_value_from_stream(self, stream: BytesIO, header_size: int):
        stream_pos = stream.tell()

        # bada-boom, empty dict :)
        # check if this works with non-null dict
        if self.allow_none:
            flag = stream.read(1)
            # stream.seek(stream_pos)
            if flag == b'\x00':
                return None
            elif flag == b'\x01':
                # not empty dict
                pass
            else:
                stream.seek(stream_pos)

        kw = PyFixedDict(self.attributes)
        for key, _type in self.attributes.items():
            kw[key] = _type.create_from_stream(stream, header_size=header_size)
        return kw

    def _add_value_to_stream(self, stream: BytesIO, payload: dict, header_size: int):
        if self.allow_none:
            if payload is None:
                UInt8().write_to_stream(stream, 0)
            else:
                UInt8().write_to_stream(stream, 1)
        for key, _type in self.attributes.items():
            _type.write_to_stream(stream, payload[key], header_size=header_size)

    @classmethod
    def from_section(cls, alias, section: etree.ElementBase, header_size=1):
        attributes = OrderedDict()
        props: Iterable[etree.ElementBase] = section.find('Properties')
        for prop in props:
            attributes[prop.tag] = alias.get_data_type_from_section(
                prop.find('Type'))
        none_section = section.find('AllowNone')
        allow_none = none_section is not None and none_section.text.strip() == 'true'
        return cls(attributes, allow_none)

    def get_size_in_bytes(self):
        if self.allow_none:
            return INFINITY

        size = 0
        for attr, value in self.attributes.items():
            size += value.get_size_in_bytes()
        return size

    def __repr__(self):
        return "<FixedDict> {}".format({
            k: v for (k, v) in self.attributes.items()
        })


class Array(_DataType):

    SIZE_TYPE = UInt8

    def __init__(self, _type: DataType, array_size=None, allow_none=False, header_size=1):
        self.allow_none = allow_none
        self.array_size = array_size
        self.type = _type
        super(Array, self).__init__(header_size=header_size)

    def _get_value_from_stream(self, stream: BytesIO, header_size: int):
        result = PyFixedList(self.type)

        size = self.array_size
        if self.array_size is None:
            size = self.SIZE_TYPE(header_size=header_size). \
                create_from_stream(stream, header_size=header_size)

        for _ in range(size):
            result.append(self.type.create_from_stream(stream, header_size=header_size))
        return result

    def _add_value_to_stream(self, stream: BytesIO, payload: list, header_size: int):
        if self.array_size is None:
            self.SIZE_TYPE(header_size=header_size). \
                write_to_stream(stream, len(payload), header_size=header_size)

        for value in payload:
            self.type.write_to_stream(stream, value, header_size=header_size)

    @classmethod
    def from_section(cls, alias, section: etree.ElementBase, header_size):
        child_type = alias.get_data_type_from_section(
            section.find('of'))
        none_section = section.find('AllowNone')
        allow_none = none_section is not None and none_section.text.strip() == 'true'
        size_section = section.find('size')
        if size_section is not None:
            array_size = int(size_section.text.strip())
        else:
            array_size = None
        return cls(child_type, array_size=array_size, allow_none=allow_none, header_size=1)

    def get_size_in_bytes(self):
        if self.array_size is not None:
            return self.type.get_size_in_bytes() * self.array_size
        return INFINITY

    def _get_default_value_from_section(self, section: etree.ElementBase):
        """
        <Default>
            <item> 1.0 </item>
            <item> 1.0 </item>
            <item> 1.0 </item>
        </Default>
        """
        defaults = []
        for it in section.findall('item'):
            defaults.append(self.type.get_default_value(it))
        return defaults

    def __repr__(self):
        if self.array_size is not None:
            return "<Array> {}".format([self.type] * self.array_size)
        return "<Array> [{}, ...]".format(self.type)


class UserType(_DataType):
    _DATA_SIZE = INFINITY

    def __init__(self, _type: DataType, header_size=1):
        if _type is None:
            _type = Blob()
        self.type = _type
        super(UserType, self).__init__(header_size=header_size)

    def _get_value_from_stream(self, stream: BytesIO, header_size: int):
        # even if type is set as non-blob
        # we still must read header first
        # otherwise we will get padding error
        if not isinstance(self.type, Blob):
            stream.read(header_size)
        return self.type.create_from_stream(stream, header_size=header_size)

    @classmethod
    def from_section(cls, alias, section: etree.ElementBase, header_size):
        type_section = section.find('Type')
        if type_section is None:
            child_type = Blob()
        else:
            child_type = alias.get_data_type_from_section(type_section)
        return cls(child_type, header_size=1)

    def __repr__(self):
        return "<UserType> {}".format(self.type)


class Mailbox(_DataType):
    _DATA_SIZE = INFINITY

    def _get_value_from_stream(self, stream: BytesIO, header_size: int):
        # UInt8(header_size=header_size). \
        #     create_from_stream(stream, header_size=header_size)

        # return ip-port pair ('127.0.0.1', 6000)
        return (
            socket.inet_ntoa(stream.read(4)),
            struct.unpack('>H', stream.read(2))[0])

    def _add_value_to_stream(self, stream: BytesIO, payload: Tuple[str, int], header_size: int):
        # UInt8(header_size=header_size). \
        #     write_to_stream(stream, 6, header_size=header_size)

        stream.write(socket.inet_aton(payload[0]))
        stream.write(struct.pack('>H', payload[1]))

    def __repr__(self):
        return "<Mailbox>".format()
