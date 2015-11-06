import unittest
import add_numbers

class unitTest_add_numbers(unittest.TestCase):
  """testing add_numbers"""
  
  def test_add_numbers(self):
    self.assertEquals(9,add_numbers.add_numbers(4,5),"adding 4 and 5")

if __name__ == '__main__':
  unittest.main()
