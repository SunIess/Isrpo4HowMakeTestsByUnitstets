import unittest
def area(a, b):
  return a * b
def perimetr(a, b):
  return (a + b) * 2
class RectangleTestCase(unittest.TestCase):
  def test_area_zero_side(self):
    res = area(0, 10)
    self.assertEqual(res, 0)
