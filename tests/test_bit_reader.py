import unittest
from io import BytesIO

from ddt import data, unpack, ddt

from replay_unpack.core.entity_def.bit_reader import BitReader


@ddt
class TestBigReader(unittest.TestCase):

    def test_read_bits_normally_all_array(self):
        s = BytesIO(b'\x01')  # 0000 0001
        bit_reader = BitReader(s)

        self.assertEqual(0, bit_reader.get(1))
        self.assertEqual(1, bit_reader.get(7))

        self.assertEqual(b'', bit_reader.get_rest())

    def test_read_bits_normally_only_first_byte(self):
        s = BytesIO(b'\xF0\x02')  # 1111 0000 0000 0010
        bit_reader = BitReader(s)

        self.assertEqual(1, bit_reader.get(1))
        self.assertEqual(3, bit_reader.get(2))
        self.assertEqual(2, bit_reader.get(2))

        self.assertEqual(b'\x02', bit_reader.get_rest())

    def test_read_bits_normally_two_bytes(self):
        s = BytesIO(b'\xF0\x02')  # 1111 0000 0000 0010
        bit_reader = BitReader(s)

        self.assertEqual(1, bit_reader.get(1))
        self.assertEqual(3, bit_reader.get(2))
        self.assertEqual(2, bit_reader.get(2))
        self.assertEqual(0, bit_reader.get(8))
        self.assertEqual(2, bit_reader.get(3))

        self.assertEqual(b'', bit_reader.get_rest())

    @data(
        [0, 0],
        [1, 0],
        [2, 1],
        [3, 2],
        [4, 2],
        [5, 3]
    )
    @unpack
    def test_bits_requires(self, object_size, bits):
        bit_reader = BitReader('')
        self.assertEqual(bits, bit_reader.bits_required(object_size))


if __name__ == '__main__':
    unittest.main()
