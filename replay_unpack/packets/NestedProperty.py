#!/usr/bin/python
# coding=utf-8
import logging
import struct

from replay_unpack.base.decorators import bigworld_packet
from replay_unpack.base.packets.PacketData import PacketDataBase
from def_generator.nested_types import PyFixedDict, PyFixedList
from def_generator.decorators import unpack_variables
from def_generator.bit_reader import BitReader

__author__ = "Aleksandr Shyshatsky"


@bigworld_packet(type_=34)
class NestedProperty(PacketDataBase):
    def __init__(self, stream):
        self.entity_id, = struct.unpack('I', stream.read(4))
        self.is_slice = struct.unpack('b', stream.read(1))[0] == 1
        self.payload_size, = struct.unpack('b', stream.read(1))

        self.u = stream.read(3)  # unknown
        self.payload = stream.read()
        assert len(self.payload) == self.payload_size

    def read_and_apply(self, entity):
        bit_reader = BitReader(self.payload)
        obj = entity

        while bit_reader.get(1) and obj:
            l = len(obj.attributesMap) if hasattr(obj, 'attributesMap') else len(obj)
            max_bits = BitReader.bits_required(l)
            property_id = bit_reader.get(max_bits)
            if hasattr(obj, 'get_field_name_for_index'):
                field = obj.get_field_name_for_index(property_id)
                obj = obj[field]
            elif hasattr(obj, 'attributesMap'):
                field = obj.attributesMap[property_id]
                obj = getattr(obj, field)
            else:
                raise NotImplementedError
            logging.debug('next path item: %s(%s)', field, property_id)

        logging.debug('object: %s %s', obj, type(obj))

        if isinstance(obj, PyFixedDict):
            assert self.is_slice is False
            max_bits = BitReader.bits_required(len(obj))
            index1 = bit_reader.get(max_bits)

            field = obj.get_field_name_for_index(index1)
            logging.debug('old obj[%s] = %s', field, obj[field])
            obj[field] = unpack_variables(bit_reader.get_rest(), [obj.get_field_type_for_index(index1)])[0]
            logging.debug('new obj[%s] = %s', field, obj[field])

        elif isinstance(obj, PyFixedList):
            if self.is_slice:
                max_bits = BitReader.bits_required(len(obj) + 1)
            else:
                max_bits = BitReader.bits_required(len(obj))
            index1 = bit_reader.get(max_bits)
            logging.debug('Bits per array index: %s', max_bits)
            logging.debug('List index: %s', index1)
            if self.is_slice:
                index2 = bit_reader.get(max_bits)
                logging.debug('Slice index: %s', index2)

            rest = bit_reader.get_rest()
            if not rest:
                logging.debug('empty response, bytes read %s', bit_reader.bytes_read)
                if self.is_slice:
                    logging.debug('removing element %s', obj[index1:index2])
                    obj[index1:index2] = []
                else:
                    obj[index1] = None
                return
            t = unpack_variables(rest, [obj.get_element_type()])
            logging.debug('new list object: %s', t)

            if self.is_slice:
                obj[index1:index1] = t
            else:
                obj[index1] = t[0]

        else:
            raise NotImplementedError
