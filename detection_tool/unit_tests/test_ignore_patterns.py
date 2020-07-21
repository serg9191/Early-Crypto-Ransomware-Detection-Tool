import unittest
import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from ignore_patterns import IgnorePatterns

class TestIgnorePatterns(unittest.TestCase):
  # The setup before each test method 
  def setUp(self):
    """Initialise IgnorePatterns class with empty list,
    use premade values
    args:
      [] (list) : empty list of ignore patterns
    """    
    self.ignore_patterns_premade = IgnorePatterns([])

    ignore_patterns = ['test']
    """Initialise IgnorePatterns class with predifined list,
    use custom values
    args:
      [] (list) : list containing ignore patterns
    """      
    self.ignore_patterns_custom = IgnorePatterns(ignore_patterns)

  # This method tests IgnorePatterns constructor
  def test_constructor(self):
    expected_nr_of_ignore_patterns_premade = 2
    # Get number of elements in the premade ignore patterns list
    actual_nr_of_ignore_patterns = len(self.ignore_patterns_premade.ignore_patterns)
    # compare expected against actual number of elements
    self.assertEqual(expected_nr_of_ignore_patterns_premade,
      actual_nr_of_ignore_patterns)
 
    # Repeat same steps for custom
    expected_nr_of_ignore_patterns_custom = 1
    actual_nr_of_ignore_patterns = len(self.ignore_patterns_custom.ignore_patterns)
    self.assertEqual(expected_nr_of_ignore_patterns_custom,
      actual_nr_of_ignore_patterns)

  # This method tests IgnorePatterns.add_ignore_pattern function
  def test_add_ignore_pattern(self):
    # Add new entry to the list
    self.ignore_patterns_premade.add_ignore_pattern("test")
    # Evalute entry existance in the list and store evaluation as boolean
    added = "test" in self.ignore_patterns_premade.ignore_patterns
    # Compare evaluation value against expected
    self.assertEqual(True, added)

  def test_get_ignore_patterns(self):
    # Expected values of the ignore patterns premade list
    expected = self.ignore_patterns_premade.ignore_patterns
    # Actual values of the ignore patterns premade list
    actual = self.ignore_patterns_premade.get_ignore_patterns()
    # Compare expected against actual
    self.assertEqual(expected, actual)

  def test_delete_ignore_pattern(self):
    # Add new entry to the list
    self.ignore_patterns_premade.add_ignore_pattern("test")
    # Delete entry from the list
    self.ignore_patterns_premade.delete_ignore_pattern("test")
    # Evalute entry existance in the list and store evaluation as boolean
    delete_status = "test" in self.ignore_patterns_premade.ignore_patterns
    # Compare evaluation value against expected
    self.assertEqual(False, delete_status)


if __name__ == '__main__':
  unittest.main()