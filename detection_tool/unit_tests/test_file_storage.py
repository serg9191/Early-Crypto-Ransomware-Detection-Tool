import copy
import os
import unittest
import sys
sys.path.insert(1, '..')

from file import File
# This is the Class that is being tested
from file_storage import FileStorage
from detection_indicators import DetectionIndicators

class TestFileStorage(unittest.TestCase):
  # The setup before each test method   
  def setUp(self):
    # Mock values to be passed to File class constructor
    file_name = "file_name"
    file_path = "C:/Desktop/my_dir/file_name"
    file_extension = "txt"
    absolute_path = "C:/Desktop/my_dir/file_name.txt"
    # An object of type DetectionIndicators
    detection_indicators = DetectionIndicators()
    """Initialise File class
    args:
      file_name (str) : file name
      file_path (str) : file path
      file_extension (str) : file extension
      absolute_path (str) : absolute path
      detection_indicators(DetectionIndicators): object of type DetectionIndicators      
    """ 
    self.file = File(file_name, file_path, file_extension,
      absolute_path, detection_indicators)
    """Initialise FileStorage class
    args:
      [] (list) : an empty list to store files
    """     
    self.file_storage = FileStorage([])

  # This method test FileStorage constructor
  def test_constructor(self):
    # Get actual values of the file storage class fields
    # that are passed to constructor
    expected = self.file_storage.list_of_files
    actual = []
    # Compare actual against expected, after class initialisation
    self.assertEqual(expected, actual)

  # This method tests FileStorage.add_new_file function
  def test_add_new_file(self):
    expected = 1
    # Add new entry to the list
    self.file_storage.add_new_file(self.file)
    # Compare expected number of entries against actual
    actual = len(self.file_storage.list_of_files)
    self.assertEqual(expected, actual)

  # This method tests FileStorage.get_all_files function
  def test_get_all_files(self):
    expected_nr_of_file = 1
    # Add new entry to the file storage list
    self.file_storage.add_new_file(self.file)
    # Get actual number of entries
    actual_nr_of_files = len(self.file_storage.get_all_files())
    # Get actual content of the list
    actual_content = self.file_storage.get_all_files()
    # Expected content of the list
    expected_conter = [self.file]
    # Compare expected against actual
    self.assertEqual(expected_nr_of_file, actual_nr_of_files)
    self.assertEqual(actual_content, expected_conter)

  # This method tests FileStorage.get_file_from_storage function
  def test_get_file_from_storage(self):
    # Add new entry to the file storage list
    self.file_storage.add_new_file(self.file)
    # Absolute path of the newly added file
    src = self.file.absolute_path
    # Get return value of the function that is tested while
    # passing computed source.
    actual_file = self.file_storage.get_file_from_storage(src)
    # Expected return value of the function
    expected_file = self.file
    # Compare expected against actual
    self.assertEqual(expected_file, actual_file)
    non_existing_file = self.file_storage.get_file_from_storage("test")
    self.assertEqual(False, non_existing_file)

  # This method tests FileStorage.delete_file_from_storage function
  def test_delete_file_from_storage(self):
    # Add new entry to the file storage list
    self.file_storage.add_new_file(self.file)
    # Delete new entry from the file storage list
    self.file_storage.delete_file_from_storage(self.file)
    # Evaluate if entry is still in file storage list and store
    # evaluation as boolean
    deleted = self.file in self.file_storage.list_of_files
    # Compare expected against actual
    self.assertEqual(False, deleted)#

  def test_find_similar_file(self):
    # Add new entry to the file storage list
    self.file_storage.add_new_file(self.file)
    expected_return_value_of_function = False
    actual_return_value_of_function = self.file_storage.find_similar_file(self.file.absolute_path)
    # Compare expected versus actual. Expected value would be False as no
    # similar file in the storage
    self.assertEqual(expected_return_value_of_function, actual_return_value_of_function)

    # Make a copy of existing file within the storage
    mock_file = copy.deepcopy(self.file)
    # Alter the way that mock ransomware would
    mock_file.change_file_extension(mock_file, ".aes")
    mock_file.change_absolute_path(mock_file, "C:/Desktop/my_dir/file_name.aes")
    expected_return_value_of_function = self.file
    actual_return_value_of_function = self.file_storage.find_similar_file(mock_file.absolute_path)
    # Compare expected versus actual. Expected value would be the original file
    # because all parameters except extension are the same.
    self.assertEqual(expected_return_value_of_function, actual_return_value_of_function)

if __name__ == '__main__':
  unittest.main()