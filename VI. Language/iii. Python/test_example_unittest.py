import unittest

class ExampleTestCase(unittest.TestCase):
  def setUp(self):
    # Code to set up test fixtures, if any
    pass

  def tearDown(self):
    # Code to clean up after tests
    pass

  def test_addition(self):
    self.assertEqual(1 + 1, 2)

  def test_subtraction(self):
    self.assertEqual(2 - 1, 1)

if __name__ == '__main__':
  unittest.main()
