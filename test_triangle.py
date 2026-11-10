import unittest

import triangle


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        res = triangle.area(5, 10)
        self.assertEqual(res, 25)

    def test_area_odd(self):
        res = triangle.area(3, 5)
        self.assertEqual(res, 7.5)

    def test_area_zero(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        res = triangle.perimeter(1.5, 2.5, 3)
        self.assertAlmostEqual(res, 7.0)
