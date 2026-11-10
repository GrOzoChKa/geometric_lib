import math
import unittest

import circle


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        res = circle.area(2)
        self.assertAlmostEqual(res, 4 * math.pi)

    def test_area_one(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = circle.area(0.5)
        self.assertAlmostEqual(res, 0.25 * math.pi)

    def test_perimeter(self):
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 6 * math.pi)

    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
