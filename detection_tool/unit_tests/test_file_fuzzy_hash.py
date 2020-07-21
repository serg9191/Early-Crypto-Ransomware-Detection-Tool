import os
import unittest
import sys

sys.path.insert(1, '..')

from file import File
# This is the Class that is being tested
from file_fuzzy_hash import FileFuzzyHash
from detection_indicators import DetectionIndicators

class TestFileFuzzyHash(unittest.TestCase):
  # The initial setup before each test method
  def setUp(self):
    # Str variable initialised to mock value, file name
    file_name = "fuzzyhashtest.txt"
    # Str variable initialised to mock value, file path
    file_path = "file_path"
    # Str variable initialised to mock value, file extension
    file_extension = "extension"
    # Str variable initialised to mock value, absolute path
    absolute_path = os.path.join(os.getcwd(), "fuzzyhashtest.txt")
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
    """Initialise FileFuzzyHash class
    args:
      None
    """
    self.file_fuzzy_hash = FileFuzzyHash()

  # This method tests compute_fuzzy_hash function.
  # The aim is to test if clause rather then ssdeep library
  # that computes fuzzy hash.
  def test_compute_fuzzy_hash(self):
    # To address first condition, create file larger than 4KiB.
    # Fuzzy hash should be computed and added.
    with open("test_over_4kb.txt", "wb") as f:
      f.truncate(1024 * 4)
    self.file.absolute_path = "test_over_4kb.txt"     
    self.file_fuzzy_hash.compute_fuzzy_hash(self.file)
    fuzzy_hash_computed = len(self.file.file_fuzzy_hash) > 0
    self.assertEqual(fuzzy_hash_computed, True)

    # To address second condition, create file smaller than 4KiB
    # Fuzzy hash list should be cleared.
    with open("test_under_4kb.txt", "wb") as f:
      f.truncate(1024 * 1)
    self.file.absolute_path = "test_under_4kb.txt"
    self.file_fuzzy_hash.compute_fuzzy_hash(self.file)    
    fuzzy_hash_not_computed = len(self.file.file_fuzzy_hash) == 0
    self.assertEqual(fuzzy_hash_not_computed, True)

    os.remove("test_over_4kb.txt")
    os.remove("test_under_4kb.txt")

  # This method tests compare_fuzzy_hash function
  def test_compare_fuzzy_hash(self):
    # Create file with some data
    with open("fuzzyhashtest.txt","w+") as f1:
      f1.truncate(1024 * 4)

    # Compure fuzzy hash
    self.file_fuzzy_hash.compute_fuzzy_hash(self.file)
    # Expected score None because only one entry, nothing to compare
    expected_score = None
    # Get comparesement evaluation score
    actual_score = self.file_fuzzy_hash.compare_fuzzy_hash(self.file)
    # Compare expected against actual
    self.assertEqual(expected_score, actual_score)

    # Compute second fuzzy hash on the same file
    self.file_fuzzy_hash.compute_fuzzy_hash(self.file)
    # Expected score is 100 because hash computed on non changed file
    expected_score = 100
    # Get comparesement evaluation score
    actual_score = self.file_fuzzy_hash.compare_fuzzy_hash(self.file)
    # Compare expected against actual
    self.assertEqual(expected_score, actual_score)

    # Delete created file
    os.remove("fuzzyhashtest.txt")

if __name__ == '__main__':
  unittest.main()    