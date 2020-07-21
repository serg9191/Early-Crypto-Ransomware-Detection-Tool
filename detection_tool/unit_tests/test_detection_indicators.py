import unittest
import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from detection_indicators import DetectionIndicators

class TestDetectionIndicators(unittest.TestCase):
  # The setup before each test method   
  def setUp(self):
    """Initialise DetectionIndicators class with empty params
    """       
    self.detection_indicators = DetectionIndicators()

  # This method test DetectionIndicators constructor
  def test_constructor(self):
    # The class field that are initialised upon class instantiation
    # are stored in local variables
    actual_entropy_violation = self.detection_indicators.entropy_violation
    actual_file_type_change = self.detection_indicators.file_type_change
    actual_similarity_violation = self.detection_indicators.similarity_violation
    actual_evaluation_score = self.detection_indicators.evaluation_score

    # Set of variables containing expected values
    expected_entropy_violation = False
    expected_file_type_change = False
    expected_similarity_violation = False
    expected_evaluation_score = 0

    # Compare actual against expected values
    self.assertEqual(actual_entropy_violation, expected_entropy_violation)
    self.assertEqual(actual_file_type_change, expected_file_type_change)
    self.assertEqual(actual_similarity_violation, expected_similarity_violation)
    self.assertEqual(actual_evaluation_score, expected_evaluation_score)

  # This method tests correctness of excessive_entropy function
  def test_excessive_entropy(self):
    # Initial value of field entropy_violation originally set to false,
    # changed to true by the below method
    self.detection_indicators.excessive_entropy()
    # Extract actual field value and store expected value
    actual_entropy_violation = self.detection_indicators.entropy_violation
    expected_entropy_violation = True
    # Compare actual versus expected
    self.assertEqual(actual_entropy_violation, expected_entropy_violation)
    
  # This method tests correctness of file_type_change function
  def test_file_type_changed(self):
    # Initial value of field file_type_change originally set to false,
    # changed to true by the below method    
    self.detection_indicators.file_type_changed()
    # Extract actual field value and store expected value
    actual_file_type_change = self.detection_indicators.file_type_change
    expected_file_type_change = True
    # Compare actual versus expected
    self.assertEqual(actual_file_type_change, expected_file_type_change)

  # This method tests correctness of file_type_change function
  def test_dissimilar_hash(self):
    # Initial value of field similarity_violation originally set to false,
    # changed to true by the below method    
    self.detection_indicators.dissimilar_hash()
    # Extract actual field value and store expected value    
    actual_similarity_violation = self.detection_indicators.similarity_violation
    expected_similarity_violation = True
    # Compare actual versus expected    
    self.assertEqual(actual_similarity_violation, expected_similarity_violation)
    
  # This method tests correctness of detection_indicators_triggered function
  def test_detection_indicators_triggered(self):
    # DetectionIndicators.evaluation_score may have four states 0;1;2;3.
    # loop iterates four times, loop value is expected score.
    # Upon each iteration one detection indicator triggered.
    # Finally, compare actual versus expected score of tuple.
    for i in range(0, 4):
      expected_score = i
      actual_score = i
      if i == 1:
        self.detection_indicators.excessive_entropy()
      if i == 2:
        self.detection_indicators.file_type_changed()
      if i == 3:
        self.detection_indicators.dissimilar_hash()
      actual_score = self.detection_indicators.detection_evaluation_score()[0]
      self.assertEqual(expected_score, actual_score)

  # This method tests correctness of the associate_score_with_descriptor function
  def test_associate_score_with_descriptor(self):
    # Set of possible descriptors
    no_indicators = "no ransomware detected"
    single_indicator = "unlikely"
    double_indicator = "possibly"
    union_indicators = "ransomware detected"
    # Similar logic as previous unit test, except this time
    # descriptor of tuple being compared rather than score.
    for i in range(0, 4):
      expected_descriptor = no_indicators
      if i == 1:
        self.detection_indicators.excessive_entropy()
        expected_descriptor = single_indicator
      if i == 2:
        self.detection_indicators.file_type_changed()
        expected_descriptor = double_indicator
      if i == 3:
        self.detection_indicators.dissimilar_hash()
        expected_descriptor = union_indicators
      actual_descriptor = self.detection_indicators.detection_evaluation_score()[1]
      self.assertEqual(expected_descriptor, actual_descriptor)

if __name__ == '__main__':
  unittest.main()