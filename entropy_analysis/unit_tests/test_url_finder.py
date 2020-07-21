import unittest


import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from url_finder import UrlFinder

class TestUrlFinder(unittest.TestCase):

  # The setup before each test method 
  def setUp(self):
    """Initialise UrlFinder class
    args:
      pdf (str) : file extension in questions
      1   (int) : desired number of results
    """
    self.url_finder = UrlFinder('pdf', 1) 
    # Initialise variable random_url (str)
    # Multiple tests will be performed against this variable
    self.random_url = """https://www.insightinvestment.com/globalassets
                  /documents/fund-and-strategy-profiles
                  /global-abs-fund.pdf"""    

  # This method tests UrlFinder.query_search_engine mothod
  def test_query_search_engine(self):
    # Execute UrlFinder method
    self.url_finder.query_search_engine()
    """A test is performed below against condition:
    url_finder.query_search_engine should have produces
    1 * 3 results with the extensions 'pdf'.
    Test checks if number of results matches
    expected number of the results.
    """
    self.assertEqual(len(self.url_finder.url_list), 3)

  # This method tests UrlFinder.get_all_users method 
  def test_get_all_users(self):
    """This assertion should return false as
    no search has been conducted
    """
    self.assertFalse(self.url_finder.url_list)

  # This method tests UrlFinder.extension_match method
  def test_extension_match(self):
    """This assertion should evaluate to true as
    random_url variable has an extension pdf,
    same as argument when class initialised
    """
    self.assertEqual(True, self.url_finder.extension_match(self.random_url))

  # This method test UrlFinder.request_complete method
  def test_request_complete(self):
    """ This assertion should evaluate to false as
    url_finder.url_list is empty, when expected value
    should be 3
    """
    self.assertEqual(False, self.url_finder.request_complete())

if __name__ == '__main__':
  unittest.main()