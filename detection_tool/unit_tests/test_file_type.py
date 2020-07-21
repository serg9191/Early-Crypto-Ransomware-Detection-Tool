import unittest
import sys
import os

sys.path.insert(1, '..')

from file import File
# This is the Class that is being tested
from file_type import FileType
from detection_indicators import DetectionIndicators

class TestFileType(unittest.TestCase):
  # The initial setup before each test method
  def setUp(self):
    # Str variable initialised to mock value, file name
    file_name = "file_type.txt"
    # Str variable initialised to mock value, file path
    file_path = "file_path"
    # Str variable initialised to mock value, file extension
    file_extension = "extension"
    # Str variable initialised to mock value, absolute path
    absolute_path = os.path.join(os.getcwd(), "file_type.txt")
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
    self.file = File(file_name, file_path, file_extension, absolute_path,
      detection_indicators)
    """Initialise FileType class
    args:
      None
    """
    self.file_type = FileType()  

  def test_determine_file_type(self):
    # Create file with some data
    with open("file_type.txt","w+") as f1:
      f1.write("abcdefg")

    # Determine file type
    self.file_type.determine_file_type(self.file)

    # Validate that the pre-objecte initialisation value of
    # empty string has been replaced
    file_type_has_been_initialised = self.file.file_type != ""
    self.assertEqual(file_type_has_been_initialised, True)

    # change file_type value manually
    self.file.file_type = "will not change"
    # Try to compute file type, this should fail as previous
    # instruction crafted value
    self.file_type.determine_file_type(self.file)
    file_type_reading_failed = self.file.file_type == "will not change"
    # assert the expectation
    self.assertEqual(file_type_reading_failed, True)
    # delete created test file
    os.remove("file_type.txt")

  def test_compare_file_type(self):
    # Create file with some data
    with open("file_type.txt","w+") as f1:
      f1.write("abcdefg")

    # Determine file type
    self.file_type.determine_file_type(self.file)
    # Should return false as file type did not change
    file_did_not_change = self.file_type.compare_file_type(self.file)
    self.assertEqual(file_did_not_change, False)

    # delete created test file
    os.remove("file_type.txt")    


if __name__ == '__main__':
  unittest.main()    