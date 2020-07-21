class IgnorePatterns:
  """
  A class to store and manipulate ignored patterns.
  This class is a helper class for observer.

  Attributes
  ---
  ignore_patterns : list
    A list to store ignore patterns.
    Initialised to the argument passed to
    the constructor or assigned premade values.

  Methods
  ---
  get_ignore_patterns()
    This method returns a list of ignore patterns
  delete_ignore_pattern()
    This method deletes specified ignore pattern
  add_ignore_pattern()
    This method adds new ignore pattern to the list  
  """  
  def __init__(self, ignore_patterns):
    """
    Parameters
    ----------
    ignore_patterns : list
      a list containing patterns that if found
      in the file absolute path then file
      should be ignore.
    """         
    if not ignore_patterns:
      self.ignore_patterns = ['*/~*', '~*']
    else:
      self.ignore_patterns = ignore_patterns

  # This method return a list of ignore patterns
  def get_ignore_patterns(self):
    return self.ignore_patterns

  # This method removes specified ignore pattern
  # from the list 
  def delete_ignore_pattern(self, ignore_pattern):
    if ignore_pattern in self.ignore_patterns:
      self.ignore_patterns.remove(ignore_pattern)
      print("Ignore pattern " + str(ignore_pattern) + " removed from list")
    else:
      print("Ignore pattern not found")

  # This method adds specified ignore pattern to the list
  def add_ignore_pattern(self, ignore_pattern):
    self.ignore_patterns.append(ignore_pattern)
