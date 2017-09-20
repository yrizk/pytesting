"""Tests for calc."""
import unittest

def add(x, y):
  return x + y

def subtract(x, y):
  return  x - y

class CalcTest(unittest.TestCase):

  def test_add_simple(self):
    self.assertEqual(add(5,4), 9)

  def test_subtract_simple(self):
    self.assertEquals(subtract(3, 4), -2)

if __name__ == "__main__":
  unittest.main()