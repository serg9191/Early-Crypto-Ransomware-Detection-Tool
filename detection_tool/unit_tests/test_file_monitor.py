import unittest
import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
import file_monitor as fm
from file import File
from detection_indicators import DetectionIndicators
from file_entropy import FileEntropy

class TestFileMonitor(unittest.TestCase):
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

  # This method tests FileMonitor.ignore_temp_files function
  def test_ignore_temp_files(self):
    # Mock value with the extension .tmp
    source = "C:/Users/sgore/Desktop/look_up_with_entropy/test_files.tmp"
    # .tmp input processed by the function should return True.
    self.assertEqual(True, fm.ignore_temp_files(source))

  # This method tests FileMonitor.get_list_of_temp_data_folders function
  def test_get_list_of_temp_data_folders(self):
    # Compute expected values, these values are known
    # due to device ownership and windows archiutecture.
    expected_1 = "C:\\Windows\\Temp"
    expected_2 = "C:\\sgore\\AppData\\Local\\Temp"

    # Get actual values returned by the method
    actual = fm.get_list_of_temp_data_folders()

    actual_1 = actual[0]
    actual_2 = actual[1]

    # Compare exptected against actual
    self.assertEqual(expected_1, actual_1)
    self.assertEqual(expected_2, actual_2)

  # This method tests if entropy_threshold_violation
  # correctly evaluates entropy threshold and returns
  # boolean according to evaluation
  def test_entropy_threshold_violation(self):
    file_entropy = FileEntropy([], 5)

    # Three blocks, for each file type.
    # Logic of each block is same:
    # initialise entropy to excessive value, compare,
    # initialise to acceptable value, compare.
    excess_entropy = 6.38584796206
    acceptable_entropy = 6.38584796205
    file_entropy.entropy = excess_entropy
    self.file.file_entropies.append(file_entropy)
    self.file.file_type = "text"
    expected_evaluation = True
    actual_evaluation = fm.entropy_threshold_violation(self.file)
    self.assertEqual(expected_evaluation, actual_evaluation)
    self.file.file_entropies[-1].entropy = acceptable_entropy
    expected_evaluation = False
    actual_evaluation = fm.entropy_threshold_violation(self.file)
    self.assertEqual(expected_evaluation, actual_evaluation)

    excess_entropy = 7.82340025468
    acceptable_entropy = 7.82340025467
    file_entropy.entropy = excess_entropy
    self.file.file_entropies.append(file_entropy)
    self.file.file_type = "word"
    expected_evaluation = True
    actual_evaluation = fm.entropy_threshold_violation(self.file)
    self.assertEqual(expected_evaluation, actual_evaluation)
    self.file.file_entropies[-1].entropy = acceptable_entropy
    expected_evaluation = False
    actual_evaluation = fm.entropy_threshold_violation(self.file)
    self.assertEqual(expected_evaluation, actual_evaluation)

    excess_entropy = 7.85799058407
    acceptable_entropy = 7.85799058406
    file_entropy.entropy = excess_entropy
    self.file.file_entropies.append(file_entropy)
    self.file.file_type = "pdf"
    expected_evaluation = True
    actual_evaluation = fm.entropy_threshold_violation(self.file)
    self.assertEqual(expected_evaluation, actual_evaluation)
    self.file.file_entropies[-1].entropy = acceptable_entropy
    expected_evaluation = False
    actual_evaluation = fm.entropy_threshold_violation(self.file)
    self.assertEqual(expected_evaluation, actual_evaluation) 
  
if __name__ == '__main__':
  unittest.main()