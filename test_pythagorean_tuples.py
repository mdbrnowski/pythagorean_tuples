import math
import unittest
from random import randint

from pythagorean_tuples import pythagorean_triples


def is_pythagorean_triple(t):
    return t[0] ** 2 + t[1] ** 2 == t[2] ** 2


def is_primitive(t):
    return math.gcd(t[0], t[1]) == 1 and math.gcd(t[1], t[2]) == 1 and math.gcd(t[2], t[0]) == 1


class TestPythagoreanTriples(unittest.TestCase):
    def test_not_integer(self):
        self.assertRaises(TypeError, pythagorean_triples, 3.14, "TypeError has not been raised")

    def test_not_positive(self):
        self.assertRaises(ValueError, pythagorean_triples, 0, "ValueError has not been raised")

    def test_number_AP(self):
        self.assertEqual(set(), pythagorean_triples(2, True))
        self.assertEqual({(4, 3, 5)}, pythagorean_triples(4, True))
        self.assertEqual({(32, 255, 257)}, pythagorean_triples(32, True))
        self.assertEqual({(512, 65535, 65537)}, pythagorean_triples(512, True))

    def test_number_A(self):
        self.assertEqual(set(), pythagorean_triples(2))
        self.assertEqual({(4, 3, 5)}, pythagorean_triples(4))
        self.assertEqual({(32, 24, 40), (32, 60, 68), (32, 126, 130), (32, 255, 257)}, pythagorean_triples(32))
        self.assertEqual({(512, 384, 640), (512, 960, 1088), (512, 2016, 2080), (512, 4080, 4112), (512, 8184, 8200),
                          (512, 16380, 16388), (512, 32766, 32770), (512, 65535, 65537)}, pythagorean_triples(512))

    def test_random_AP(self):
        for _ in range(10):
            a = 2 ** randint(15, 50)
            primitive_triples = pythagorean_triples(a, True)
            for t in primitive_triples:
                self.assertTrue(is_pythagorean_triple(t), f"{t} is not Pythagorean triple")
                self.assertTrue(is_primitive(t), f'{t} is not primitive')

    def test_random_A(self):
        for _ in range(10):
            a = 2 ** randint(15, 50)
            triples = pythagorean_triples(a)
            for t in triples:
                self.assertTrue(is_pythagorean_triple(t), f"{t} is not Pythagorean triple")

    def test_number_BP(self):
        self.assertEqual({(3, 4, 5)}, pythagorean_triples(3, True))
        self.assertEqual({(13, 84, 85)}, pythagorean_triples(13, True))
        self.assertEqual({(271, 36720, 36721)}, pythagorean_triples(271, True))
        self.assertEqual({(121, 7320, 7321)}, pythagorean_triples(121, True))
        self.assertEqual({(153, 104, 185), (153, 11704, 11705)}, pythagorean_triples(153, True))
        self.assertEqual({(235, 1092, 1117), (235, 27612, 27613)}, pythagorean_triples(235, True))

    def test_number_B(self):
        self.assertEqual({(3, 4, 5)}, pythagorean_triples(3))
        self.assertEqual({(13, 84, 85)}, pythagorean_triples(13))
        self.assertEqual({(271, 36720, 36721)}, pythagorean_triples(271))
        self.assertEqual({(121, 660, 671), (121, 7320, 7321)}, pythagorean_triples(121))
        self.assertEqual({(153, 104, 185), (153, 204, 255), (153, 420, 447), (153, 680, 697), (153, 1296, 1305),
                          (153, 3900, 3903), (153, 11704, 11705)}, pythagorean_triples(153))
        self.assertEqual({(235, 564, 611), (235, 1092, 1117), (235, 5520, 5525), (235, 27612, 27613)},
                         pythagorean_triples(235))

    def test_random_BP(self):
        for _ in range(10):
            a = randint(10_000_000, 100_000_000) * 2 + 1
            primitive_triples = pythagorean_triples(a, True)
            for t in primitive_triples:
                self.assertTrue(is_pythagorean_triple(t), f"{t} is not Pythagorean triple")
                self.assertTrue(is_primitive(t), f'{t} is not primitive')

    def test_random_B(self):
        for _ in range(10):
            a = randint(10_000_000, 100_000_000) * 2 + 1
            triples = pythagorean_triples(a)
            for t in triples:
                self.assertTrue(is_pythagorean_triple(t), f"{t} is not Pythagorean triple")

    def test_number_CP(self):
        self.assertEqual({(12, 5, 13), (12, 35, 37)}, pythagorean_triples(12, True))
        self.assertEqual(set(), pythagorean_triples(14, True))
        self.assertEqual(set(), pythagorean_triples(34, True))
        self.assertEqual({(56, 33, 65), (56, 783, 785)}, pythagorean_triples(56, True))
        self.assertEqual({(68, 285, 293), (68, 1155, 1157)}, pythagorean_triples(68, True))
        self.assertEqual(set(), pythagorean_triples(126, True))

    def test_number_C(self):
        self.assertEqual({(12, 5, 13), (12, 35, 37), (12, 9, 15), (12, 16, 20)}, pythagorean_triples(12))
        self.assertEqual({(14, 48, 50)}, pythagorean_triples(14))
        self.assertEqual({(34, 288, 290)}, pythagorean_triples(34))
        self.assertEqual({(56, 33, 65), (56, 42, 70), (56, 90, 106), (56, 105, 119), (56, 192, 200), (56, 390, 394),
                          (56, 783, 785)}, pythagorean_triples(56))
        self.assertEqual({(68, 51, 85), (68, 285, 293), (68, 576, 580), (68, 1155, 1157)},
                         pythagorean_triples(68))
        self.assertEqual({(126, 32, 130), (126, 120, 174), (126, 168, 210), (126, 432, 450), (126, 560, 574),
                          (126, 1320, 1326), (126, 3968, 3970)}, pythagorean_triples(126))

    def test_random_CP(self):
        for _ in range(10):
            a = randint(10_000_000, 100_000_000) * 2
            primitive_triples = pythagorean_triples(a, True)
            for t in primitive_triples:
                self.assertTrue(is_pythagorean_triple(t), f"{t} is not Pythagorean triple")
                self.assertTrue(is_primitive(t), f'{t} is not primitive')

    def test_random_C(self):
        for _ in range(10):
            a = randint(10_000_000, 100_000_000) * 2
            triples = pythagorean_triples(a)
            for t in triples:
                self.assertTrue(is_pythagorean_triple(t), f"{t} is not Pythagorean triple")


if __name__ == '__main__':
    unittest.main()
