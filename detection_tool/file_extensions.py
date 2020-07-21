class FileExtensions:
  """
  A class to store target file extension as
  well as file extensions to observe.

  Attributes
  ---
  targeted_file_extensions : list
    a list to store targeted file extensions
  observable_file_extensions : list
    a list to store file extensions that
    are later passed to observer for observation.

  Methods
  ---
  add_targeted_file_extensions()
    This method adds tageted file extension
    according to the specifid argument
  print_targeted_file_extensions()
    This method prints all targeted file
    extensions
  get_all_targeted_file_extensions()
    This method return list of targeted
    file extensions
  delete_targeted_file_extension()
    This method deletes targeted files extension
    from the tatrgeted file extension list
    according to specified extension as argument
  add_observable_file_extensions()
    This method adds observable file extension
    according to the given argument
  print_observable_file_extensions()
    This method prints all observable file
    extensions
  get_all_observable_file_extensions()
    This method return list of observable
    file extensions
  delete_observable_file_extension()
    This method deletes observable files extension
    from the observable file extension list
    according to the given argument
  """  
  def __init__(self, targeted_file_extensions, observable_file_extensions):
    """
    Parameters
    ----------
    targeted_file_extensions : list
      list containing targeted file extensions
    observable_file_extensions : list
      list containing observable file extensions    
    """

    # if targeted_file_extensions passed to the constructor
    # is empty, then pre-defined targeted file extensions are
    # used.
    if not targeted_file_extensions:
      self.targeted_file_extensions = [
      'pdf',
      'odt',
      'docx',
      'pptx',
      'txt',
      'mov',
      'zip',
      'md',
      'nmid',
      'opml',
      'pages',
      'jpg',
      'xls',
      'csv',
      'doc',
      'ppt',
      'git',
      'png',
      'xml',
      'html',
      'xlsx',
      'mp3',
      'jpf',
      'log',
      'ogg',
      'wav'
      ]
    else:
      self.targeted_file_extensions = targeted_file_extensions

    # if observable_file_extensions passed to the constructor
    # is empty, then pre-defined observable file extensions are
    # used.
    if not observable_file_extensions:
      self.observable_file_extensions = [
      '*.pdf',
      '*.odt',
      '*.docx',
      '*.pptx',
      '*.txt',
      '*.mov',
      '*.zip',
      '*.md',
      '*.nmid',
      '*.opml',
      '*.pages',
      '*.jpg',
      '*.xls',
      '*.csv',
      '*.doc',
      '*.ppt',
      '*.git',
      '*.png',
      '*.xml',
      '*.html',
      '*.xlsx',
      '*.mp3',
      '*.jpf',
      '*.log',
      '*.ogg',
      '*.wav',
      '*.aes'
      ]
    else:
      self.observable_file_extensions = observable_file_extensions      

  # This method adds given argument to the liss of targeted
  # file extensions.
  def add_targeted_file_extensions(self, file_extension):
    self.targeted_file_extensions.append(file_extension)

  # This method prints each targeted extension.
  def print_targeted_file_extensions(self):
    for file_extension in self.targeted_file_extensions:
      print(file_extension)

  # This method returns list of targeted extensions
  def get_all_targeted_file_extensions(self):
    return self.targeted_file_extensions

  # This method deletes given argument from the list
  # of targeted file extensions.
  def delete_targeted_file_extension(self, file_extension):
    # If the passed argument exists in the list - delete,
    # otherwise print message.
    if file_extension in self.targeted_file_extensions:
      self.targeted_file_extensions.remove(file_extension)
      print("File extension " + str(file_extension) + " removed from list")
    else:
      print("File extension not found")

  # This method adds given argument to the liss of observable
  # file extensions.
  def add_observable_file_extensions(self, observable_file_extension):
    self.observable_file_extensions.append(observable_file_extension)

  # This method prints each observable extension.
  def print_observable_file_extensions(self):
    for file_extension in self.observable_file_extensions:
      print(file_extension)

  # This method returns list of observable extensions
  def get_all_observable_file_extensions(self):
    return self.observable_file_extensions

  # This method deletes given argument from the list
  # of observable file extensions.
  def delete_observable_file_extension(self, observable_file_extension):
    # If the passed argument exists in the list - delete,
    # otherwise print message.    
    if observable_file_extension in self.observable_file_extensions:
      self.observable_file_extensions.remove(observable_file_extension)
      print("File extension " + str(observable_file_extension) + " removed from list")
    else:
      print("File extension not found")