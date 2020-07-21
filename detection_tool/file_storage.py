from file import File

import os

class FileStorage():
  """
  A class that implements file storage.

  Attributes
  ---
  list_of_files : list
    a list to store objects of File type
  Methods
  ---
  add_new_file()
    This method adds new entry to the file
    storage according to given argument.
  print_all_files()
    This method prints all files in the storage
  get_all_files()
    This method returns list of all files
  get_file_from_storage()
    This method returnes specified file according to
    given argument
  delete_file_from_storage()
    This method deletes file from the storage
    according to given argument          
    """ 
  def __init__(self, list_of_files):
    """
    Parameters
    ----------
    list_of_files : list
      a list of files, either populated
      or empty.
    """       
    self.list_of_files = list_of_files

  # This method takes give file as an argument
  # and appends to the file storage
  def add_new_file(self, file):
    self.list_of_files.append(file)

  # This method prints each file withing the storage
  def print_all_files(self):
    for file in self.list_of_files:
      print(file.to_string())

  # This method returns list of all files
  def get_all_files(self):
    return self.list_of_files

  # This method takes file path as an argument,
  # looks up the file and returns it if
  # file exists in the storage. Otherwise,
  # return false
  def get_file_from_storage(self, src):
    for file in self.list_of_files:
      if file.absolute_path == src:    
        return file 
    return False

  # This method looks up ancestor file of its new encrypted version.
  # Method functionality is restricted to specific encryption format,
  # it is not dynamic approach that would work for anay situation.
  # For simplicity it is tailored to work for particular cases, namely,
  # mock ransomware.
  def find_similar_file(self, src):
    src_file_extension = os.path.splitext(src)[1]
    if src_file_extension == ".aes":
      src_file_name = os.path.basename(src).replace(src_file_extension, "") 
      src_file_path = os.path.splitext(src)[0]
      for file in self.list_of_files:
        file_path = file.file_path
        file_extension = file.file_extension
        file_name = file.file_name.replace(file_extension, "")         
        if (src_file_name == file_name and src_file_path == file_path and
          src_file_extension != file_extension):
          return file
    return False                        

  # This method deletes file from the storage.
  # It looks up file passed as an argument in the file
  # storage, if found deletes.
  def delete_file_from_storage(self, file):
    if file in self.list_of_files:
      self.list_of_files.remove(file)
      print("Following file remove from storage:")
      print(file.to_string())
    else:
      print("file not found. Failed deleting file")