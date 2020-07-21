import calendar
import requests
import os
import shutil
import time
import urllib.request
import uuid

from url_finder     import UrlFinder
from urllib.request import Request, urlopen 

class UrlDownloader:
  """
  A class used to implement get/doownload request
  based on the given urls.

  Attributes
  ---
  url_finder : UrlFinder
    an object of type UrlFinder
  path_to_download_dir : str
    a string indicating path to download directory

  Methods
  ---
  start_download()
    downloads file one by one from the given url list
  create_folder()
    sets up the download folder
  """
  def __init__(self, url_finder):
    """
    Parameters
    ----------
    url_finder : UrlFinder
      an object of type UrlFinder

    Raises
    ------
    RequestException
      any possible http exception that is not
      specified in below exceptions.
    HTTPexception
      if http exception occurs such as HTTP 403
      error, access forbidden
    Connectionexception
      for any type for exception that is caused
      by the connection
    Timeout
      should connection reach timeout, according
      to the set timeout   
    """       
    self.url_finder   = url_finder
    self.path_to_download_dir  = ""

  # This method downloads files from the given url
  def start_download(self):
    # Validate if list of urls empty, if not, continue
    # with the download
    if not self.url_finder.get_all_urls():
      return

    # Set up a download folder
    self.create_folder()

    # Counter to stop download when number of search
    # requests/downloads as specified
    counter = 0

    # Main loop that iterate through each url in the
    # list and downloads files
    for url in self.url_finder.get_all_urls():
      # conditional check to terminate the loop.
      # Required as list carries overhead compared
      # to number of search results
      if counter == self.url_finder.num_of_results:
        break

      # Try block.
      try:
      	# Generate a random file name
        filename = str(uuid.uuid4().hex) + "." + self.url_finder.extension        
        # Variable to store get request on the specified url, while enforcing
        # ssl certificate validation within set timeout
        result = requests.get(url, verify=True, timeout=3)
        # Check if get request caused any error 
        result.raise_for_status()
        # Compose absolute path for the downloaded file
        absolute_path = (self.path_to_download_dir +
                        "/" + str(filename))
        # Write downloaded file
        with open(absolute_path, "wb") as fout:
          fout.write(result.content)

        print("Downloaded: " + str(url))
        counter += 1
      # Exception block for varios HTTP request exception 
      except requests.exceptions.RequestException as exception:
        print(exception)
      except requests.exceptions.HTTPError as exception:
        print(exception)
      except requests.exceptions.ConnectionError as exception:
        print(exception)
      except requests.exceptions.Timeout as exception:
        print(exception)     
  
  # This method creates folder under the specified path
  def create_folder(self):
    # Set variable value to current dir along with extensions in question
    self.path_to_download_dir = os.path.join(os.getcwd() + "/downloads", self.url_finder.extension)
    # Try block to clear content of the download folder.
    # May throw exception if does not exist
    try:
      shutil.rmtree(self.path_to_download_dir)
    except:
       print("exception in " + self.path_to_download_dir +  """  during the attempt to
        delete dir content, probably does not exist""")
    # Create folder under the given path, even if it already exists
    os.makedirs(self.path_to_download_dir, exist_ok = True)