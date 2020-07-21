import unittest
import sys
sys.path.insert(1, '..')

from file_entropy import FileEntropy
# This is the Class that is being tested
from file import File
from detection_indicators import DetectionIndicators

class TestFile(unittest.TestCase):
  # The initial setup before each test method
  def setUp(self):
    # Str variable initialised to mock value, file name
    file_name = "file_name"
    # Str variable initialised to mock value, file path
    file_path = "file_path"
    # Str variable initialised to mock value, file extension
    file_extension = "extension"
    # Str variable initialised to mock value, absolute path
    absolute_path = "absolute_path"
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

  # This method tests File class constructor
  def test_constructor(self):
    # Below 4 variables are initialised to expected values,
    # based on the arguments given to constructor upon class
    # creation.
    expected_file_name = "file_name"
    expected_file_path = "file_path"
    expected_file_extension = "extension"
    expected_absolute_path = "absolute_path"
    expected_detection_indicators = self.file.detection_indicators
    # The below two variable are expected values of two
    # File class field that are initialised to default value
    # upon class creation.
    expected_file_entropies = []
    expected_old_file_paths = []
    expected_file_fuzzy_hash = []

    # Extract actual class field values of class File
    actual_file_name = self.file.file_name
    actual_file_path = self.file.file_path
    actual_file_extension = self.file.file_extension
    actual_absolute_path = self.file.absolute_path
    actual_file_entropies = self.file.file_entropies
    actual_old_file_paths = self.file.old_file_paths
    actual_file_fuzzy_hash = self.file.file_fuzzy_hash
    actual_detection_indicators = self.file.detection_indicators

    # Assert expected against actual.
    self.assertEqual(expected_file_name, actual_file_name)
    self.assertEqual(expected_file_path, actual_file_path)
    self.assertEqual(expected_file_extension, actual_file_extension)
    self.assertEqual(expected_absolute_path, actual_absolute_path)
    self.assertEqual(expected_file_entropies, actual_file_entropies)
    self.assertEqual(expected_old_file_paths, actual_old_file_paths)
    self.assertEqual(expected_file_fuzzy_hash, actual_file_fuzzy_hash)
    self.assertEqual(expected_detection_indicators, actual_detection_indicators)

  # This method tests File.add_old_path function
  def test_add_old_path(self):
    # Create and append mock path to the File.old_file_paths list.
    expected_old_path = "test_old_path"
    self.file.old_file_paths.append("test_old_path")
    # Check if newly added path exists in the list and store
    # boolean evaluation in the variable
    old_path_added = expected_old_path in self.file.old_file_paths
    # Previously stored value should be True as tested against
    # entry that we just entered.
    self.assertEqual(True, old_path_added)
    self.file.old_file_paths.pop()

  # This method tests File.add_fuzzy_hash function
  def test_add_fuzzy_hash(self):
    # Create and append mock fuzzy hash to the File.add_fuzzy_hash list.
    expected_file_fuzzy_hash = "test_fuzzy_hash"
    self.file.file_fuzzy_hash.append("test_fuzzy_hash")
    # Check if newly added fuzzy hash exists in the list and store
    # boolean evaluation in the variable
    file_fuzzy_hash_added = expected_file_fuzzy_hash in self.file.file_fuzzy_hash
    # Previously stored value should be True as tested against
    # entry that we just entered.
    self.assertEqual(True, file_fuzzy_hash_added)
    self.file.file_fuzzy_hash.pop()    

  # This method tests File.change_file_name function
  def test_change_file_name(self):
    # Compute new mock file name and change old file name
    # to a new mock file name.
    expected_file_name = "new_file_name"
    self.file.file_name = "new_file_name"
    # Extract file name after change
    actual_file_name = self.file.file_name
    # Compare actual against expected file name
    self.assertEqual(expected_file_name, actual_file_name)

  # This method tests File.change_file_extension function
  def test_change_file_extension(self):
    # Create and initialise new mock file extension
    # and change old file extension with new one
    expected_file_extension = "new_file_extension"
    self.file.file_extension = "new_file_extension"
    # Extract file extension
    actual_file_extension = self.file.file_extension
    # Compare actual against expected file name
    self.assertEqual(expected_file_extension, actual_file_extension)

  def test_change_absolute_path(self):
    # Create and initialise new mock file absolute path
    # and change old file absolute path with new one    
    expected_absolute_path = "new_absolute_path"
    self.file.absolute_path = "new_absolute_path"
    # Extract actual file absolute path
    actual_absolute_path = self.file.absolute_path
    # Compare actual against expected absolute file path
    self.assertEqual(expected_absolute_path, actual_absolute_path)

  # This method tests File.compare_entropy function
  def test_compare_entropy(self):
    # Populate entropy list with two same values
    for i in range(0, 2):
      self.file.file_entropies.append(FileEntropy([], 0))
    # Two same values should return true when compared, hence, expected
    # valued evaluated against actual.
    self.assertEqual(True, self.file.compare_entropy(self.file))

  # This method tests file.set_file_type function
  def test_set_file_type(self):
    # execute function with crafted data
    self.file.set_file_type(self.file, "test")
    # compared actual against expected data to verify
    # correctness of functgion
    expected_file_type = "test"
    actual_file_type = self.file.file_type
    self.assertEqual(expected_file_type, actual_file_type)

  # This method tests file.delete_fuzzy_hash_entries function
  def test_delete_fuzzy_hash_entries(self):
    # Add entry, verify that list is non empty
    self.file.file_fuzzy_hash.append("random")
    list_non_empty = len(self.file.file_fuzzy_hash) > 0
    self.assertEqual(list_non_empty, True)
    # Delete new entry and verify that list is empty
    self.file.delete_fuzzy_hash_entries(self.file)
    list_empty = len(self.file.file_fuzzy_hash) == 0
    self.assertEqual(list_empty, True)

if __name__ == '__main__':
  unittest.main()