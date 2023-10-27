import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
    def test2(self):
        actual = Triangle.classify(7, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def test3(self):
        actual = Triangle.classify(10, 10, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def test4(self):
        actual = Triangle.classify(10, 7, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    def test5(self):
        actual = Triangle.classify(10, 11, 12)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    def test6(self):
        actual = Triangle.classify(-1, 0, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test7(self):
        actual = Triangle.classify(4, 30, 100)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test8(self):
        actual = Triangle.classify(-1, -10, -20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test9(self):
        actual = Triangle.classify(1, 1, -0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test10(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test11(self):
        actual = Triangle.classify(5, 100, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test12(self):
        actual = Triangle.classify(5, 5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test13(self):
        actual = Triangle.classify(10, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test14(self):
        actual = Triangle.classify(1, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test15(self):
        actual = Triangle.classify(0, -1, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test16(self):
        actual = Triangle.classify(0, 0, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test17(self):
        actual = Triangle.classify(-1, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test18(self):
        actual = Triangle.classify(5, 1, 100)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test19(self):
        actual = Triangle.classify(1, 5, 100)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test20(self):
        actual = Triangle.classify(100, 1, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test21(self):
        actual = Triangle.classify(0, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test22(self):
        actual = Triangle.classify(1, 0, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
