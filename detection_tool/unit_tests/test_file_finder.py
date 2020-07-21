import json
import os
import unittest
import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from file_finder import FileFinder

class TestDriveFinder(unittest.TestCase):
  # The setup before each test method     
  def setUp(self):
    arg1 = "targeted_file_extensions"
    arg2 = "list_of_all_drives"
    arg3 = "ignore_dirs"
    arg4 = "file_storage"
    """Initialise DriveFinder class
    args:
      arg1 (str) : mock value
      arg2 (str) : mock value
      arg3 (str) : mock value
      arg4 (str) : mock value
    """    
    self.file_finder = FileFinder(arg1, arg2, arg3, arg4)    

  # This method tests DriveFinder constructor
  def test_constructor(self):
    # Initialise variable to expected values of DriveFinder
    # class fields
    expected_targeted_file_extensions = "targeted_file_extensions"
    expected_list_of_all_drives = "list_of_all_drives"
    expected_ignore_dirs = "ignore_dirs"
    expected_file_storage = "file_storage"

    # Get actual values of DriveFinder class fields
    actual_targeted_file_extensions = self.file_finder.targeted_file_extensions
    actual_list_of_all_drives = self.file_finder.list_of_all_drives
    actual_ignore_dirs = self.file_finder.ignore_dirs
    actual_file_storage = self.file_finder.file_storage

    # Evaluate actual against expected
    self.assertEqual(expected_targeted_file_extensions, actual_targeted_file_extensions)
    self.assertEqual(expected_list_of_all_drives, actual_list_of_all_drives)
    self.assertEqual(expected_ignore_dirs, actual_ignore_dirs)
    self.assertEqual(expected_file_storage, actual_file_storage)

  # This method test DriveFinder.break_source_into_substrings function
  def test_break_source_into_substrings(self):
    # Mock file path
    source = "C:/Users/sgore/Desktop/look_up_with_entropy/test_files"

    # Break down mock file path into substring.
    # This mimics the internals of the break_source_into_substrings
    # function.
    expected_file_name = os.path.basename(source)
    expected_file_path = os.path.splitext(source)[0]
    expected_file_extension = os.path.splitext(source)[1]
    expected_absolute_path = source

    # Get actual return values of the function
    actual = json.loads(self.file_finder.break_source_into_substrings(source))

    actual_file_name = actual['file_name']
    actual_file_path = actual['file_path']
    actual_file_extension = actual['file_extension']
    actual_absolute_path = actual['absolute_path']

    # Evaluate expected - manually computed values aginst
    # actual values returned by the function 
    self.assertEqual(expected_file_name, actual_file_name)
    self.assertEqual(expected_file_path, actual_file_path)
    self.assertEqual(expected_file_extension, actual_file_extension)
    self.assertEqual(expected_absolute_path, actual_absolute_path)

if __name__ == '__main__':
  unittest.main()