import textwrap

class File:
  """
  A class used to to describe file

  Attributes
  ---
  file_name: str
    A string containing file basename
  file_path: str
    A string containing file path
  file_extension: str
    A string containing file extension
  absolute_path: str
    A string containing full file path
  file_entropies: list
    A list to store FileEntropy objects
  old_file_paths: list
    A list to store all file move locations
  file_fuzzy_hash: list
    A list containing fuzzy hashes
  file_type: string
    A string contraining initial reading
    of a file type
  detection_indicators: DetectionIndicators
    A field to store DetectionIndicators object         

  Methods
  ---
  minimal_to_string()
    returns formatted textual representation
    of the object
  to_string()
    return full textual representation of
    the object
  compare_entropy(url)
    compares old entropy against new entropy
  add_old_path()
    adds old file path to the old_file_paths
    list
  add_fuzzy_hash()
    adds fuzzy file hash to the file_fuzzy_hash
    list    
  change_file_name()
    method to change file name
  change_file_path()
    method to change file path
  change_file_extension()
    method to change file extension
  change_absolute_path()
    method to change full file name with path
  set_file_type()
    this method sets empty file_type variable
    to a given valued            
  """    
  def __init__(self, file_name, file_path, file_extension, absolute_path,
    detection_indicators):
    """
    Parameters
    ----------
    file_name : str
      The file name
    file_path : str
      The file path
    file_extension : str
      The file extension
    absolute_path : str
      The full file path with name
    detection_indicators : DetectionIndicators
      Object of type DetectionIndicators      
    """     
    self.file_name       = file_name
    self.file_path       = file_path
    self.file_extension  = file_extension
    self.absolute_path   = absolute_path
    self.file_entropies  = []
    self.old_file_paths  = []
    self.file_fuzzy_hash = []
    self.file_type       = ""
    self.detection_indicators = detection_indicators

    # This method implements file format to produce
    # minimal string representation of the object, namely
    # file name and most recent file entropy
  def minimal_to_string(self):
    if len(self.file_entropies) == 0:
        return textwrap.dedent(
            """\
            file_name: {0}
            """.format(
            self.file_name))
    return textwrap.dedent(
        """\
        file_name: {0},
        {1}
        """.format(
        self.file_name,
        self.file_entropies[-1].to_string()))    

    # This method implements file format to produce
    # string representation of the object, namely,
    # all its fields, except old file paths. To
    # produce entropy textual representation, call to
    # entropy object method is made.
  def to_string(self):
    if len(self.file_entropies) == 0:
        return textwrap.dedent(
            """\
            file_name: {0}
            file_path: {1}
            file_extension: {2}
            absolute_path: {3}
            """.format(
            self.file_name,
            self.file_path,
            self.file_extension,
            self.absolute_path))

    return textwrap.dedent(
        """\
        file_name: {0}
        file_path: {1}
        file_extension: {2}
        absolute_path: {3}
        file_entropies: {4}
        """.format(
        self.file_name,
        self.file_path,
        self.file_extension,
        self.absolute_path,
        self.file_entropies[-1].to_string()))

    # This methood compares current entropy against
    # previous entropy. Before hand, it validates
    # if the list contains more than 1 record.
    # Return boolean dependin on evaluation status.
  def compare_entropy(self, file):
    if len(file.file_entropies) > 1:
        print("new entropy=" + str(file.file_entropies[-1].entropy) + " old entropy=" + str(file.file_entropies[-2].entropy))
        if file.file_entropies[-2].time_when_entropy_measured != file.file_entropies[-1].time_when_entropy_measured:
            if file.file_entropies[-1].entropy != file.file_entropies[-2].entropy:
              return False
    return True

    # This method append old file path to the list
  def add_old_path(self, file):
    self.old_file_paths.append(file.absolute_path)

    # This method append fuzzy file hash to the list
  def add_fuzzy_hash(self, file, fuzzy_hash):
    file.file_fuzzy_hash.append(fuzzy_hash)

    # This method deletes all fuzzy file hash entries
  def delete_fuzzy_hash_entries(self, file):
    del file.file_fuzzy_hash[:]

    # This method changes file name of a given
    #  file object that is passed as argument
  def change_file_name(self, file, file_name):
    file.file_name = file_name

    # This method changes file path of a given
    #  file object that is passed as argument
  def change_file_path(self, file, file_path):
    file.file_path = file_path

    # This method changes file extension of a given
    #  file object that is passed as argument
  def change_file_extension(self, file, file_extension):
    file.file_extension = file_extension

    # This method changes file name and path of a given
    #  file object that is passed as argument
  def change_absolute_path(self, file, absolute_path):
    file.absolute_path = absolute_path

    # This method sets file_type attribute according
    # to the given value of variable file_type
  def set_file_type(self, file, file_type):
    file.file_type = file_type