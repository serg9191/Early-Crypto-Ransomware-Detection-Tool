import getpass
import os
import time
import sys


# The interface switch between versions of File Monitor.
# File Monitor version started according to supplied argv or as default.
full_version = False
limited_version = False

if (len(sys.argv) > 1):
  if sys.argv[1] == "full_version":
    print("""WARNING: Full version only scans the system for files.
Detection Indicators have been disabled due to File Monitor Limitations.""")
    while True:
      print("Are you sure you want to run this version? y/n")
      answer = input()
      if answer.lower() == "y" or answer.lower() == "n":
        if answer.lower() == "y":
          print("Starting File Monitor in Full Version.")
          print("Scanning Entire System for Files")
          full_version = True
          break          
        if answer.lower() == "n":
          break

      if answer.lower() != "y" or answer.lower() != "n":
        continue

if len(sys.argv) < 2 or full_version == False or sys.argv[1] == "limited_version":
  limited_version = True
  print("Starting File Monitor in Limited Version.")
  print("Scanning File Monitor Home Directory for Files")    


if full_version:
  from drive_finder        import DriveFinder    
from file_extensions     import FileExtensions
from file_finder         import FileFinder
from file_entropy        import FileEntropy
from file_storage        import FileStorage
from file_fuzzy_hash     import FileFuzzyHash
from file_type           import FileType
from ignore_patterns     import IgnorePatterns

from tqdm import tqdm

from watchdog.observers  import Observer
from watchdog.events     import PatternMatchingEventHandler

class FileMonitor(PatternMatchingEventHandler):
  """
  A class used to implement Watchdog library to
  observe file state

  Attributes
  ---
  file_storage : FileStorage
    an object of type FileStorage
  file_finder : FileFinder
    an object of type FileFinder
  file_fuzzy_hash : FileFuzzyHash
    an object of type FileFuzzyHash
  file_type : FileType
    an object of type FileType

  Methods
  ---
  on_created()
    This method tracks any file creation events.
  on_deleted()
    This method tracks any file deletion events.  
  on_modified()
    This method tracks any file modifications.
  on_moved()
    This method tracks any file move events.
  """  
  def __init__(self, patterns, ignore_patterns, file_storage, file_finder,
    file_fuzzy_hash, file_type):
    super().__init__(patterns, ignore_patterns)
    """
    Parameters
    ----------
    patterns : list
      file extensions to observe
    ignore_patterns : list
      file name patterns to ignore       
    file_storage : UrlFinder
      an object of type UrlFinder
    file_finder : FileFinder
      an object of type FileFinder
    file_fuzzy_hash : FileFuzzyHash
      an object of type FileFuzzyHash
    file_type : FileType
      an object of type FileType                      
    """       
    self.file_storage = file_storage
    self.file_finder  = file_finder
    self.file_fuzzy_hash = file_fuzzy_hash
    self.file_type = file_type

  # This method is triggered when file is created.
  # Upon file creation, file source processed,
  # new File object created and appended to the file storage.
  # In addition, file entropy calculated.
  def on_created(self, event):
    self.file_finder.process_new_file(event.src_path)
    file = get_file(self.file_storage, event.src_path)
    if not file:
      return
    else:
      similar_file = self.file_storage.find_similar_file(file.absolute_path)
      if similar_file == False:
        calculate_entropy(file)
        self.file_fuzzy_hash.compute_fuzzy_hash(file)
        self.file_type.determine_file_type(file)
      else:
        file.file_entropies = similar_file.file_entropies
        file.file_fuzzy_hash = similar_file.file_fuzzy_hash
        file.file_type = similar_file.file_type
        file.detection_indicators = similar_file.detection_indicators        

  # This method is triggered when file is deleted.
  # First retrieve file from file storage according
  # to the file path using get_file method.
  # If returned value false, do nothing, otherwise
  # remove from the file storage. 
  def on_deleted(self, event):
    file = get_file(self.file_storage, event.src_path)
    if not file:
      return
    else:      
      self.file_storage.delete_file_from_storage(file)

  # This method is triggered when file is modified.
  # If modified file exists within file storage, then
  # file entropy is recalculated and compared against
  # previous measure.
  def on_modified(self, event):   
    file = get_file(self.file_storage, event.src_path)
    if not file:
      return
    else:
      calculate_entropy(file)
      compare_entropy(file)
      self.file_fuzzy_hash.compute_fuzzy_hash(file)
      similarity_score = self.file_fuzzy_hash.compare_fuzzy_hash(file)
      compare_similary_hash(file, similarity_score)
      compare_file_type(file, self.file_type.compare_file_type(file))
      print(file.detection_indicators.detection_evaluation_score())
      print()

  # This method is triggered when file is move.
  # If file move occurs in ignore folder, then
  # do nothing. Otherwise, find file and change its
  # absolute path.
  def on_moved(self, event):
    if ignore_temp_files(event.dest_path):
      return
    file = get_file(self.file_storage, event.src_path)
    if not file:
      return
    else:  
      self.file_finder.rename_or_change_file_source(file, event.dest_path)    

def main():
  if full_version:
    drive_finder = DriveFinder([])              
    drive_finder.identify_device_drives()       
    drive_finder.normalize_device_drive_output()


  file_extensions = FileExtensions([], []) 

  limit_lookup_to_specific_folder = '.'

  file_storage = FileStorage([])

  ignore_patterns = IgnorePatterns([])

  if full_version:
    file_finder = FileFinder(file_extensions.get_all_targeted_file_extensions(),
                    drive_finder.get_all_device_drives(), get_list_of_temp_data_folders(),
                    file_storage)

  if limited_version:                        
    file_finder = FileFinder(file_extensions.get_all_targeted_file_extensions(),
                    limit_lookup_to_specific_folder, get_list_of_temp_data_folders(),
                    file_storage)


  print("Starting file lookup, please wait...")
  file_finder.lookup_files()
  print("File lookup finished")

  file_fuzzy_hash = FileFuzzyHash()
  file_type = FileType()

  print("Starting to compute entropy, type and fuzzy hash for all identified files, please wait...")

  progress_bar = tqdm(file_finder.file_storage.get_all_files())

  for file in progress_bar:
    progress_bar.set_description("Computing File: " + file.file_name)
    calculate_entropy(file)
    file_fuzzy_hash.compute_fuzzy_hash(file)
    file_type.determine_file_type(file)    

  print("Data for all files has been computed")    

  # initialisation of file observer  
  file_monitor = FileMonitor(file_extensions.get_all_observable_file_extensions(),
                  ignore_patterns.get_ignore_patterns(), file_storage, file_finder,
                  file_fuzzy_hash, file_type)
  observer = Observer()
  observer.schedule(file_monitor, path=str(os.getcwd()), recursive=True)
  print("Observing directory: " + str(os.getcwd()))
  observer.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

# This method returns boolean acording to evaluation if
# file is of temp type.
def ignore_temp_files(absolute_path):
  return os.path.splitext(absolute_path)[1] == ".tmp"

# This method returns file from storage with the
# help of get_file_from_storage method of FileStorage object
def get_file(file_storage, src):
  return file_storage.get_file_from_storage(src)

# This method unites all the steps required to
# calculate file entropy. Once calculated,
# appended to the list.
def calculate_entropy(file):
  file_as_byte_array = read_file(file.absolute_path)
  file_size = find_file_size(file_as_byte_array)
  file_entropy = FileEntropy(file_as_byte_array, file_size)
  file_entropy.calculate_frequency_of_bytes()
  file_entropy.calculate_file_entropy()
  file.file_entropies.append(file_entropy)

# This method returns size of the file/byte-array
def find_file_size(file_as_byte_array):
  return len(file_as_byte_array)

# This file reads the file and stores its data into
# the byte-array
def read_file(src_file_to_read):
  file_size = os.path.getsize(src_file_to_read)
  f = open(src_file_to_read, 'rb')
  file_as_byte_array = bytearray(f.read(file_size))
  f.close()
  return file_as_byte_array

# This mmethod identifies and returns regestered device users
def find_device_user():
  return str(os.path.join(getpass.getuser()))

# This method returns list of the common
# Windows directories that contain temp files
def get_list_of_temp_data_folders():
  windows_temp_data_folder = "C:\\Windows\\Temp"
  user_temp_data_folder = "C:\\" + find_device_user() + "\\AppData\\Local\\Temp"
  ignore_folders = [windows_temp_data_folder, user_temp_data_folder]
  return ignore_folders

# This method implements entropy comparisement with the help
# of compare_entropy method of File object.
# Perform action according to the evaluation.
def compare_entropy(file):
  comp_cond = file.compare_entropy(file)
  if not comp_cond:
    if entropy_threshold_violation(file):
      file.detection_indicators.excessive_entropy()
      print("entropy violation")

# This method compares similarity score.
# If similarity score zero, then corresponding
# event is being triggered.
def compare_similary_hash(file, similarity_score):
  if similarity_score != None:
    if similarity_score <= 0:
      file.detection_indicators.dissimilar_hash()
      print("similarity violation")

# This method sets file_type indicator to true
# according to comparison values.
def compare_file_type(file, compare_condition):
  if compare_condition:
    file.detection_indicators.file_type_changed()
    print("file type violation")

# This method checks if specific file type entropy
# has exceeded the violation threshold and returns
# boolean.
def entropy_threshold_violation(file):
  txt_files_threshold = 6.38584796206
  pdf_files_threshold = 7.85799058407
  docx_files_threshold = 7.82340025468
  if "word" in file.file_type.lower():
    if file.file_entropies[-1].entropy >= docx_files_threshold:
      return True
  if "text" in file.file_type.lower():
    if file.file_entropies[-1].entropy >= txt_files_threshold:
      return True    
  if "pdf" in file.file_type.lower():
    if file.file_entropies[-1].entropy >= pdf_files_threshold:
      return True
  return False

if __name__== "__main__":
  main()