import unittest
import os

import sys
sys.path.insert(1, '..')

# This is the Class that is being tested
from url_downloader import UrlDownloader
from url_finder     import UrlFinder


class TestUrlDownloader(unittest.TestCase):

  # The initial setup before each test method
  def setUp(self):
    # Initialise variable look_up_extension with the lookup value
    look_up_extension = "pdf"
    # Initialise variable number_of_search_results with the
    # number of desired search results
    number_of_search_results = 1
    # Initialise UrlFinder class, passing two previous params as args
    self.url_finder = UrlFinder(look_up_extension, number_of_search_results)
    # Execute UrlFinder.query_search_engine method to perform search
    self.url_finder.query_search_engine()
    """Initialise UrlFinder class
    args:
      url_finder (obj) : specialised class
    """
    self.url_downloader = UrlDownloader(self.url_finder)

  # This method tests UrlDownloader.start_download method 
  def test_start_download(self):
    # Initialise variable and assign value to it:
    # directory path where downloaded files live
    directory_path = os.path.join(os.getcwd() + "/downloads",
                  self.url_finder.extension)

    """Below two lines form an assertion:
    dir_empty variable assigned boolen value of
    conditional check;
    Test checks that the directory is empty prior to download
    """
    dir_empty = len(os.listdir(directory_path)) == 0
    self.assertEqual(True, dir_empty)

    self.url_downloader.start_download()

    """Below two lines form an assertion:
    dir_not_empty variable assigned boolen value of
    conditional check;
    Test checks that the directory contains files after download
    """
    dir_not_empty = len(os.listdir(directory_path)) > 0
    self.assertEqual(True, dir_not_empty)

    # Below tests if desired number of files to be downloaded
    # correctly fulfilled
    self.assertEqual(self.url_finder.num_of_results,
                    len(os.listdir(directory_path)))

  # This method tests UrlDownloader.create_folder method 
  def test_create_folder(self):
    # Execute UrlDownloader.create_folder method
    self.url_downloader.create_folder()
    # Perform check if folder exists, should return true
    # as create_folder method has been executed
    self.assertEqual(True, os.path.isdir(os.path.join(os.getcwd()  + "/downloads",
                self.url_finder.extension)))    

if __name__ == '__main__':
  unittest.main()