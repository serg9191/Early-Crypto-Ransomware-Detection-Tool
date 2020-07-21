import math
import os
import unittest
import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from file_entropy import FileEntropy

class TestFileEntropy(unittest.TestCase):
  def setUp(self):
    file_as_byte_array = []
    file_size = 5
    self.path_to_file = os.path.join(os.getcwd(), "test.txt")
    
    self.file_entropy = FileEntropy(file_as_byte_array, file_size)

  # This method tests FileEntropy constructor
  def test_constructor(self):
    # Create and initialised variables with the expected values as
    # FileEntropy class fields
    expected_file_as_byte_array = []
    expected_file_size = 5
    expected_entropy = 0
    expected_frequency_list = []
    expected_time_when_entropy_measured = 0

    # Get actual fields of class FileEntropy
    actual_file_as_byte_array = self.file_entropy.file_as_byte_array
    actual_file_size = self.file_entropy.file_size
    actual_entropy = self.file_entropy.entropy
    actual_frequency_list = self.file_entropy.frequency_list
    actual_time_when_entropy_measured = self.file_entropy.time_when_entropy_measured

    # Compare expected against actual
    self.assertEqual(expected_file_as_byte_array, actual_file_as_byte_array)
    self.assertEqual(expected_file_size, actual_file_size)
    self.assertEqual(expected_entropy, actual_entropy)
    self.assertEqual(expected_frequency_list, actual_frequency_list)
    self.assertEqual(expected_time_when_entropy_measured, actual_time_when_entropy_measured)

  # This method tests FileEntropy.calculate_frequency_of_bytes function
  def test_calculate_frequency_of_bytes(self):
    # Clean up the file
    open(self.path_to_file, 'w').close()
    # Compose a file as well as writing into it string "abcd"
    with open(self.path_to_file, 'a+') as file:
      file.write('abcd')
    # determine filesize
    self.file_entropy.file_entropy = os.path.getsize(self.path_to_file)
    # Convert file into byte array
    f = open(self.path_to_file, 'rb')
    self.file_entropy.file_as_byte_array = bytearray(f.read(self.file_entropy.file_size))
    f.close()
    # Call function that is being tested and store return value in the variable
    self.file_entropy.calculate_frequency_of_bytes()
    # Knowing content of the file and mapping of letter to decimals
    # in ascii table, we can the test actual value under the index
    # against the expected value
    for i in range(0, 4):
      expected_value = float(1) / self.file_entropy.file_size
      actual_value = self.file_entropy.frequency_list[97 + i]
      self.assertEqual(expected_value, actual_value)
    # delete created test file
    os.remove("test.txt")      

  # This method tests FileEntropy.calculate_file_entropy function
  def test_calculate_file_entropy(self):
    # Clean up the file
    open(self.path_to_file, 'w').close()
    # Compose a file as well as writing into it string "abcd"
    with open(self.path_to_file, 'a+') as file:
      file.write('abcd')

    # Determine files size, needed for frequency calculations
    self.file_entropy.file_entropy = os.path.getsize(self.path_to_file)
        # Convert file into byte array
    f = open(self.path_to_file, 'rb')
    self.file_entropy.file_as_byte_array = bytearray(f.read(self.file_entropy.file_size))
    f.close()
    # Call function that is being tested and store return value in the variable
    self.file_entropy.calculate_frequency_of_bytes()
    # Call function that is being tested and store return value in the variable
    self.file_entropy.calculate_file_entropy()
    expected_entropy = 0.0
    # Knowing content of the file we can calculate frequency; knowing frequency
    # we can calculate expected entropy and compare it against the actual entropy
    for i in range(0, 4):
      frequency_of_letter = float(1) / self.file_entropy.file_size
      expected_entropy += frequency_of_letter * math.log(frequency_of_letter, 2)
    expected_entropy = -expected_entropy
    self.assertEqual(self.file_entropy.entropy, expected_entropy)
    # delete created test file
    os.remove("test.txt")       

if __name__ == '__main__':
  unittest.main()