import random
import string

from googlesearch import search

class UrlFinder:
  """
  A class used to perform googlesearch

  Attributes
  ---
  url_list: list
    a list to contain search results
  query: str
    a correctly formed query for search
  extension: str
    the extension in question
  num_of_results: int
    the number of desired search results

  Methods
  ---
  query_search_engine()
    performs search based on the desired
    extension and nunber of search results
  get_all_urls()
    returns a list of urls
  extension_match(url)
    returns true if found url is of desired
    extension type, otherwise, false
  request_complete()
    returns true if list of same size as
    desired number of search results * 3
  """
  def __init__(self, extension, num_of_results):
    """
    Parameters
    ----------
    extension : str
      the extension in question
    num_of_results : int
      the number of desired search results
    """    
    self.url_list = []
    self.query = "filetype:"
    self.extension = extension
    self.num_of_results = num_of_results

  def query_search_engine(self):
    """Queries search engine based on the desired
    extension and number of search results
    """
    # Flag variable to halt loop
    stop = False
    # This loop performs number of queries equal to the number
    # of desired search results. Each iteration randomises
    # query by appending random postfix in order to gather
    # different search results.
    for i in range(0, self.num_of_results):
      if stop: break
      # This variable stores randomised query
      formed_random_query = (self.query +
                      self.extension +
                      " " +
                      ''.join(random.choice(string.ascii_letters)for i in range(3)))
      # Iterator to perform searches according to the given args
      # tld = top level domain
      # num = number of search results per query
      # stop = stop after n search results
      # pause = delay between searches
      # The search has a great overhead, reason - duplicate urls,
      # http errors during downloads
      for url in search(formed_random_query, tld="co.in", num=10, stop=10, pause=2):
        # Validation to check if url already in the list
        if url in self.url_list:
          pass
        # Validation to see if found url matches correct file extension format
        if self.extension_match(url): self.url_list.append(url)
        #  Validation to see if request has been fulfilled
        if self.request_complete():
          stop = True
          break

  # This method returns list of urls
  def get_all_urls(self):
    return self.url_list

  # This method matches extensions
  def extension_match(self, url):
    return url[-len(self.extension):] == self.extension

  # This method validates if request complete
  def request_complete(self):
    # Overhead in place for http download errors
    return len(self.url_list) == self.num_of_results * 3