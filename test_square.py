import unittest

import square


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = square.area(1.5)
        self.assertAlmostEqual(res, 2.25)

    def test_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
