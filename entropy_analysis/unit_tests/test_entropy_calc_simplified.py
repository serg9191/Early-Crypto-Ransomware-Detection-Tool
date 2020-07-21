import math
import os
import unittest

import sys
sys.path.insert(1, '..')

from url_finder import UrlFinder

# This is the file that is being tested
import entropy_calc_simplified as ecs

class EntropyCalcSimplified(unittest.TestCase):
  # The initial setup before each test method
  def setUp(self):
    # Initialise variable to hardcoded file path
    self.path_to_file = os.path.join(os.getcwd(), "test.txt")
    # Call  ecs method compose_file to create a file under
    # the given path
    ecs.compose_file(self.path_to_file)    

  # This method tests if the file creation was successful.
  # I am not testing python API, instead, testing if
  # the location of composed file is where expected.
  def test_compose_file(self):
    file_created = os.path.exists(self.path_to_file)
    self.assertEqual(True, file_created)

  # This method tests if method form_final_output_as_json forms
  # json format as excepted.
  def test_form_final_output_as_json(self):
    # Set of hard coded values: list, int, str and int
    frequency = [1]
    file_size = 222
    file_path = "test_path"
    entropy = 3

    # Manually form dictionary from the hardcoded values.
    # This will be the expected output of the function
    # that is being tested
    mock_json = {
    'frequency': frequency,
    'file_size': file_size,
    'file_path': file_path,
    'entropy'  : entropy
    }

    # Call function that is being tested passing same hardcoded values
    actual_json = ecs.form_final_output_as_json(
                frequency, file_size, file_path, entropy)

    # Compare expected against the actual
    self.assertEqual(mock_json, actual_json)

  # This test case checks format_frequency_list_as_json method if it
  # forms dictionary as expected
  def test_format_frequency_list_as_json(self):
    # Create mock list of size 256(ascii characters)
    mock_frequency = range(256)
    # Call function that is being tested and store return value in the variable
    frequency_json = ecs.format_frequency_list_as_json(mock_frequency)
    counter = 0
    # For every key in the dict, compare the actual key and a value
    # against expected values. Expected values are known because
    # content of the file is hardcoded.
    for key in frequency_json:
      actual_value = frequency_json[key]
      actual_key = key
      expected_key = str(chr(counter).encode('utf-8'))
      expected_value = counter
      self.assertEqual(actual_key, expected_key)
      self.assertEqual(actual_value, expected_value)
      counter += 1

  # This method tests accuracy of function calculate_frequency_of_bytes
  def test_calculate_frequency_of_bytes(self):
    # Clean up the file
    open(self.path_to_file, 'w').close()
    # Compose a file as well as writing into it string "abcd"
    ecs.compose_file(self.path_to_file)
    # Determine files size, needed for frequency calculations
    file_size = ecs.find_file_size(self.path_to_file)
    # Convert file into byte array
    file_as_byte_array = ecs.read_file(self.path_to_file)
    # Call function that is being tested and store return value in the variable
    actual_frequency = ecs.calculate_frequency_of_bytes(file_as_byte_array,
                                                        file_size)
    # Knowing content of the file and mapping of letter to decimals
    # in ascii table, we can the test actual value under the index
    # against the expected value
    for i in range(0, 4):
      expected_value = float(1) / file_size
      actual_value = actual_frequency[97 + i]
      self.assertEqual(expected_value, actual_value)

  # This method tests if calculate_entropy method produces correct calculations
  def test_calculate_entropy(self):
    # Clean up the file
    open(self.path_to_file, 'w').close()
    # Compose a file as well as writing into it string "abcd"
    ecs.compose_file(self.path_to_file)
    # Determine files size, needed for frequency calculations
    file_size = ecs.find_file_size(self.path_to_file)
    # Convert file into byte array
    file_as_byte_array = ecs.read_file(self.path_to_file)
    # Calculate byte frequency
    frequency_list = ecs.calculate_frequency_of_bytes(file_as_byte_array,
                                                      file_size)
    # Call function that is being tested and store return value in the variable
    actual_entropy = ecs.calculate_entropy(frequency_list)
    expected_entropy = 0.0
    # Knowing content of the file we can calculate frequency; knowing frequency
    # we can calculate expected entropy and compare it against the actual entropy
    for i in range(0, 4):
      frequency_of_letter = float(1) / file_size
      expected_entropy += frequency_of_letter * math.log(frequency_of_letter, 2)
    expected_entropy = -expected_entropy
    self.assertEqual(actual_entropy, expected_entropy)

# This method tests if find_average_entropy method produces correct calculations
  def test_find_average_entropy(self):
    # A variable to store sum of loop
    sum_of_i = 0
    for i in range(1, 4):
      # Increment variable by the loop value
      sum_of_i += i
      if i == 3:
        # On the final iteration of loop initialise variable of type
        # UrlFinder and pass as second argument current loop value
        url_finder = UrlFinder("test", i)
        # Call function that is being tested and store return value
        # in the variable
        actual_avg = ecs.find_average_entropy(sum_of_i, url_finder)
        # Manuall compute expected value
        expected_avg = sum_of_i / i
        # Compare actual against expected values
        self.assertEqual(actual_avg, expected_avg)

if __name__ == '__main__':
  unittest.main()