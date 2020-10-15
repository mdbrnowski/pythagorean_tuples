import math
import unittest
from random import randint

from pythagorean_tuples import pythagorean_triples


class TestExceptions(unittest.TestCase):
    def test_not_integer(self):
        self.assertRaises(TypeError, pythagorean_triples, 3.14, "TypeError has not been raised")

    def test_not_positive(self):
        self.assertRaises(ValueError, pythagorean_triples, 0, "ValueError has not been raised")


class TestAPrimitive(unittest.TestCase):
    def test_2(self):
        self.assertEqual(set(), pythagorean_triples(2, True))

    def test_4(self):
        self.assertEqual({(4, 3, 5)}, pythagorean_triples(4, True))

    def test_32(self):
        self.assertEqual({(32, 255, 257)}, pythagorean_triples(32, True))

    def test_random(self):
        res = pythagorean_triples(2 ** randint(10, 20), True)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            self.assertEqual(1, math.gcd(*t), f"{t} is not primitive")
            for n in t:
                self.assertIs(int, type(n))

    def test_random_huge(self):
        res = pythagorean_triples(2 ** randint(100, 200), True)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            self.assertEqual(1, math.gcd(*t), f"{t} is not primitive")
            for n in t:
                self.assertIs(int, type(n))


class TestA(unittest.TestCase):
    def test_2(self):
        self.assertEqual(set(), pythagorean_triples(2, False))

    def test_4(self):
        self.assertEqual({(4, 3, 5)}, pythagorean_triples(4, False))

    def test_32(self):
        self.assertEqual({(32, 24, 40), (32, 60, 68), (32, 126, 130), (32, 255, 257)}, pythagorean_triples(32, False))

    def test_random(self):
        res = pythagorean_triples(2 ** randint(10, 20), False)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            for n in t:
                self.assertIs(int, type(n))

    def test_random_huge(self):
        res = pythagorean_triples(2 ** randint(100, 200), False)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            for n in t:
                self.assertIs(int, type(n))


class TestBPrimitive(unittest.TestCase):
    def test_3(self):
        self.assertEqual({(3, 4, 5)}, pythagorean_triples(3, True))

    def test_13(self):
        self.assertEqual({(13, 84, 85)}, pythagorean_triples(13, True))

    def test_271(self):
        self.assertEqual({(271, 36720, 36721)}, pythagorean_triples(271, True))

    def test_121(self):
        self.assertEqual({(121, 7320, 7321)}, pythagorean_triples(121, True))

    def test_153(self):
        self.assertEqual({(153, 104, 185), (153, 11704, 11705)}, pythagorean_triples(153, True))

    def test_235(self):
        self.assertEqual({(235, 1092, 1117), (235, 27612, 27613)}, pythagorean_triples(235, True))

    def test_random(self):
        r = randint(10, 1000)
        while r % 2 == 0:
            r //= 2
        res = pythagorean_triples(r, True)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            self.assertEqual(1, math.gcd(*t), f"{t} is not primitive")
            for n in t:
                self.assertIs(int, type(n))

    def test_random_huge(self):
        r = randint(100, 1000000)
        while r % 2 == 0:
            r //= 2
        res = pythagorean_triples(r, True)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            self.assertEqual(1, math.gcd(*t), f"{t} is not primitive")
            for n in t:
                self.assertIs(int, type(n))


class TestB(unittest.TestCase):
    def test_3(self):
        self.assertEqual({(3, 4, 5)}, pythagorean_triples(3, False))

    def test_13(self):
        self.assertEqual({(13, 84, 85)}, pythagorean_triples(13, False))

    def test_271(self):
        self.assertEqual({(271, 36720, 36721)}, pythagorean_triples(271, False))

    def test_121(self):
        self.assertEqual({(121, 660, 671), (121, 7320, 7321)}, pythagorean_triples(121, False))

    def test_153(self):
        self.assertEqual({(153, 104, 185), (153, 204, 255), (153, 420, 447), (153, 680, 697), (153, 1296, 1305),
                          (153, 3900, 3903), (153, 11704, 11705)}, pythagorean_triples(153, False))

    def test_235(self):
        self.assertEqual({(235, 564, 611), (235, 1092, 1117), (235, 5520, 5525), (235, 27612, 27613)},
                         pythagorean_triples(235, False))

    def test_random(self):
        r = randint(10, 1000)
        while r % 2 == 0:
            r //= 2
        res = pythagorean_triples(r, False)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            for n in t:
                self.assertIs(int, type(n))

    def test_random_huge(self):
        r = randint(100, 1000000)
        while r % 2 == 0:
            r //= 2
        res = pythagorean_triples(r, False)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            for n in t:
                self.assertIs(int, type(n))


class TestCPrimitive(unittest.TestCase):
    def test_12(self):
        self.assertEqual({(12, 5, 13), (12, 35, 37)}, pythagorean_triples(12, True))

    def test_14(self):
        self.assertEqual(set(), pythagorean_triples(14, True))

    def test_34(self):
        self.assertEqual(set(), pythagorean_triples(34, True))

    def test_56(self):
        self.assertEqual({(56, 33, 65), (56, 783, 785)}, pythagorean_triples(56, True))

    def test_random(self):
        res = pythagorean_triples(randint(10, 100) * 2, True)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            self.assertEqual(1, math.gcd(*t), f"{t} is not primitive")
            for n in t:
                self.assertIs(int, type(n))

    def test_random_huge(self):
        res = pythagorean_triples(randint(100, 100000) * 2, True)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            self.assertEqual(1, math.gcd(*t), f"{t} is not primitive")
            for n in t:
                self.assertIs(int, type(n))


class TestC(unittest.TestCase):
    def test_12(self):
        self.assertEqual({(12, 5, 13), (12, 35, 37)}, pythagorean_triples(12, False))

    def test_14(self):
        self.assertEqual({(14, 48, 50)}, pythagorean_triples(14, False))

    def test_34(self):
        self.assertEqual({(34, 288, 290)}, pythagorean_triples(34, False))

    def test_56(self):
        self.assertEqual({(56, 33, 65), (56, 42, 70), (56, 90, 106), (56, 105, 119), (56, 192, 200), (56, 390, 394),
                          (56, 783, 785)}, pythagorean_triples(56, False))

    def test_random(self):
        res = pythagorean_triples(randint(10, 100) * 2, False)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            for n in t:
                self.assertIs(int, type(n))

    def test_random_huge(self):
        res = pythagorean_triples(randint(100, 100000) * 2, False)
        for t in res:
            self.assertEqual(t[2] ** 2, t[0] ** 2 + t[1] ** 2, f"{t} is not Pythagorean triple")
            for n in t:
                self.assertIs(int, type(n))


if __name__ == '__main__':
    unittest.main()
