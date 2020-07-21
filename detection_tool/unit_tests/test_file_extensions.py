import unittest
import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from file_extensions import FileExtensions

class TestDriveFinder(unittest.TestCase):
  # The setup before each test method 
  def setUp(self):
    """Initialise FileExtensions class using constructor
    default values.
    args:
      [] list : empty list for targeted file extensions
      [] list : empty list for observable file extensions
    """
    self.file_extensions_premade = FileExtensions([],[])
    file_extensions = ['file_extensions']
    observable_file_extensions = ['observable_file_extensions']
    """Initialise FileExtensions class using constructor
    passed values.
    args:
      [] list : list with targeted file extensions
      [] list : list with observable file extensions
    """    
    self.file_extensions_custom = FileExtensions(file_extensions, observable_file_extensions)

  # This method tests FileExtensions class constructor
  def test_constructor(self):
    # Expected number of default constructor values in the
    # targeted file extensions list
    expected_nr_of_file_extensions_premade = 26
    # Expected number of default constructor values in the
    # observable file extensions list    
    expected_nr_of_observable_file_extensions_premade = 27
    # Extract targeted file extensions list size
    actual_nr_of_file_extensions = len(self.file_extensions_premade.targeted_file_extensions)
    # Extract targeted file extensions list size    
    actual_nr_of_observable_file_extensions = len(self.file_extensions_premade.observable_file_extensions)

    # Compare expected against actual number of list entries
    self.assertEqual(expected_nr_of_file_extensions_premade,
      actual_nr_of_file_extensions)
    self.assertEqual(expected_nr_of_observable_file_extensions_premade,
      actual_nr_of_observable_file_extensions)

    # Same steps, except expected entries are 1 based on passed constructor args 
    expected_nr_of_file_extensions_custom = 1
    expected_nr_of_observable_file_extensions_custom = 1
    actual_nr_of_file_extensions = len(self.file_extensions_custom.targeted_file_extensions)
    actual_nr_of_observable_file_extensions = len(self.file_extensions_custom.observable_file_extensions)

    self.assertEqual(expected_nr_of_file_extensions_custom,
      actual_nr_of_file_extensions)
    self.assertEqual(expected_nr_of_observable_file_extensions_custom,
      actual_nr_of_observable_file_extensions)    

  # This method tests FileExtensions.add_targeted_file_extensions function
  def test_add_targeted_file_extensions(self):
    # Append mock value to the premade targeted file extension list
    self.file_extensions_premade.add_targeted_file_extensions("test")
    # Store boolean evaluate of mock value within the list
    added = "test" in self.file_extensions_premade.targeted_file_extensions
    # Assert expected evaluation value against actual
    self.assertEqual(True, added)

  # This method tests FileExtensions.get_all_targeted_file_extensions function
  def test_get_all_targeted_file_extensions(self):
    # Initialise expected variable with the value of FileExtension.targeted_file_extensions
    expected = self.file_extensions_premade.targeted_file_extensions
    # Store function return value in the actual value
    actual = self.file_extensions_premade.get_all_targeted_file_extensions()
    # Compare two values
    self.assertEqual(expected, actual)

  # This method tests FileExtensions.delete_targeted_file_extension function
  def test_delete_targeted_file_extension(self):
    # Add mock value to the targeted_file_extensions list
    self.file_extensions_premade.add_targeted_file_extensions("test")
    # Remove mock value from the targeted_file_extensions list
    self.file_extensions_premade.delete_targeted_file_extension("test")
    # Store boolean evaluate of mock value within the list
    delete_status = "test" in self.file_extensions_premade.targeted_file_extensions
    # Assert expected evaluation value against actual
    self.assertEqual(False, delete_status)

  # This method tests FileExtensions.add_observable_file_extensions function
  def test_add_observable_file_extensions(self):
    # Append mock value to the premade observable file extension list
    self.file_extensions_premade.add_observable_file_extensions("test")
    # Store boolean evaluate of mock value within the list
    added = "test" in self.file_extensions_premade.observable_file_extensions
    # Assert expected evaluation value against actual
    self.assertEqual(True, added)

  # This method tests FileExtensions.get_all_observable_file_extensions function
  def test_get_all_observable_file_extensions(self):
    # Initialise expected variable with the value of FileExtension.observable_file_extensions
    expected = self.file_extensions_premade.observable_file_extensions
    # Store function return value in the actual value
    actual = self.file_extensions_premade.get_all_observable_file_extensions()
    # Compare two values
    self.assertEqual(expected, actual)

  # This method tests FileExtensions.delete_observable_file_extension( function
  def test_delete_observable_file_extension(self):
    # Add mock value to the observable_file_extensions list
    self.file_extensions_premade.add_observable_file_extensions("test")
    # Remove mock value from the observable_file_extensions list
    self.file_extensions_premade.delete_observable_file_extension("test")
    # Store boolean evaluate of mock value within the list
    delete_status = "test" in self.file_extensions_premade.observable_file_extensions
    # Assert expected evaluation value against actual
    self.assertEqual(False, delete_status)

if __name__ == '__main__':
  unittest.main()