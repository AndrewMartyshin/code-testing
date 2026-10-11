import unittest
import math
import circle, triangle, square, rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rect = rectangle.area(5, 10)
        self.assertEqual(rect, 50)

    def test_perimeter(self):
        rect = rectangle.perimeter(5, 10)
        self.assertEqual(rect, 30)

    def test_zero_side(self):
        rect = rectangle.area(0, 10)
        self.assertEqual(rect, 0)

class TestSquare(unittest.TestCase):
    def test_area(self):
        sq = square.area(7)
        self.assertEqual(sq, 49)

    def test_perimeter(self):
        sq = square.perimeter(7)
        self.assertEqual(sq, 28)

class TestCircle(unittest.TestCase):
    def test_area(self):
        circ = circle.area(5)
        self.assertAlmostEqual(circ, math.pi * 25, places=5)

    def test_perimeter(self):
        circ = circle.perimeter(5)
        self.assertAlmostEqual(circ, 2 * math.pi * 5, places=5)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        tr = triangle.area(3, 4)
        self.assertAlmostEqual(tr, 6.0, places=5)

    def test_perimeter(self):
        tr = triangle.perimeter(3, 4, 5)
        self.assertEqual(tr, 12)

    def test_negative_base(self):
        tr = triangle.area(-5, 4)
        self.assertEqual(tr, -10.0)

if __name__ == '__main__':
    unittest.main()