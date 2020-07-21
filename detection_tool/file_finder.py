
import json
import os

from file import File
from detection_indicators import DetectionIndicators

class FileFinder:
  """
  This class implements file look up. Successfully
  identified files are proccessed and added to the
  FileStorage object.

  Attributes
  ---
  targeted_file_extensions : list
    a list of file extensions to look for
  list_of_all_drives : list
    a list of drives to look into
  ignore_dirs : list
    a list of directories that should be ignored
  file_storage : FileStorage object
    a file storage object to store found files

  Methods
  ---
  lookup_files()
    This method locates files
  shortlist_targeted_files()
    This method short lists all identified files
    according to specified file extensions
  process_new_file()
    This method creates new object of type File
  break_source_into_substrings()
    This method breaks down file path into:
    absolute path, file path, file extension and basename
  rename_or_change_file_source()
    This method renames or changes file path
  """
  def __init__(self, targeted_file_extensions, list_of_all_drives, ignore_dirs,
    file_storage):
    """
    Parameters
    ----------
    targeted_file_extensions : list
      a list required to shortlist found files
    list_of_all_drives : list
      a list containing device drives on which
      file look-up performed
    ignore_dirs : list
      A list containing temp dirs that should be ignored
    file_storage : FileStorage
      an object of type FileStorage                  

    """     
    self.targeted_file_extensions = targeted_file_extensions
    self.list_of_all_drives       = list_of_all_drives
    self.ignore_dirs              = ignore_dirs
    self.file_storage             = file_storage

  # This method performs file look-up 
  def lookup_files(self):
    # iterate through all identified drives and locates all files.
    for drive in self.list_of_all_drives:
      for root, dirs, files in os.walk(str(drive)):
        if root in self.ignore_dirs:
           dirs[:] = []
           files[:] = []
        else:
        # Iterate through the list of files and only take files that match
        # specified file extenstions
            self.shortlist_targeted_files(root, files, None)

  # This method short lists all found files to only specific file
  # extension
  def shortlist_targeted_files(self, root, files, list_of_files):
    for file in files:
      # Convert file path into absolute file path format
      file = os.path.join(os.path.abspath(root), file)
      # If file extension within specified targeted file extension list,
      # then processes file path according to File object constructor req.
      # This is achieved via function call break_source_into_substrings.
      # Once processed, create file and add to file storage object.
      if file.endswith(tuple(self.targeted_file_extensions)):
        file_details = json.loads(self.break_source_into_substrings(os.path.join(root, file)))
        self.file_storage.add_new_file(
          File(file_details['file_name'], file_details['file_path'],
            file_details['file_extension'], file_details['absolute_path'],
            DetectionIndicators()))    

  # This method takes files source as an argument. Processes path according to the
  # File object constructor and adds to the file storage object.
  def process_new_file(self, source):
    file_details = json.loads(self.break_source_into_substrings(source))
    self.file_storage.add_new_file(
      File(file_details['file_name'], file_details['file_path'],
        file_details['file_extension'], file_details['absolute_path'],
        DetectionIndicators())) 
    print("new file created: " + str(file_details['absolute_path']))

  # This method processes file path, and returns in json format for simplicity.
  def break_source_into_substrings(self, source):
    file_name = os.path.basename(source)
    file_path = os.path.splitext(source)[0]
    file_extension = os.path.splitext(source)[1]
    absolute_path = source
    return json.dumps({'file_name': file_name, 'file_path': file_path,
      'file_extension': file_extension,
      'absolute_path': absolute_path})

  # This method takes file and file path as an arguments.
  # Changes current file path to a new specified by the source argument.
  def rename_or_change_file_source(self, file, source):
    print("Renaming or changing source of file:")
    print(file.to_string())
    file_details = json.loads(self.break_source_into_substrings(source))

    file.change_file_name(file, file_details['file_name'])
    file.change_file_path(file, file_details['file_path'])
    file.change_file_extension(file, file_details['file_extension'])
    file.change_absolute_path(file, file_details['absolute_path'])

    print("New file name or source:")
    print(file.to_string())