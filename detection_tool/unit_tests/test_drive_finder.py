import unittest
import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from drive_finder import DriveFinder

class TestDriveFinder(unittest.TestCase):
  # The initial setup before each test method
  def setUp(self):
    """Initialise DriveFinder class
    args:
      [] (list) : the list of drives
    """    
    self.drive_finder = DriveFinder(['c', 'd'])

  # This method test DriveFinder class constructor 
  def test_constructor(self):
    # The assertion based on comparasion of
    # known value against expected value.
    expected = ['c', 'd']
    actual = self.drive_finder.list_of_all_drives
    self.assertEqual(expected, actual)

  # This method tests DriveFinder.get_all_device_drives
  # method.
  def test_get_all_device_drives(self):
    # The assertion based on comparasion of known
    # value passed to the constructor, against expected
    # return value of the method.
    expected = ['c', 'd']
    actual = self.drive_finder.get_all_device_drives()
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()