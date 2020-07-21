import os
import ssdeep

from file import File

class FileFuzzyHash:
  """
  This class implements fuzzy hash, using
  ssdeep library.

  Methods
  ---
  compute_fuzzy_hash()
    This method computes fuzzy hash with function
    call to ssdeep library. Takes file absolute
    path as an argument.
  compare_fuzzy_hash()
    This method compares previous and new fuzzy hashes
    to determine similarity of current and previous 
    version of the file.

  """  
  def __init__(self):
    None

  # This method computes fuzzy hash of the file.
  # Fuzzy hashing does not accuratly compare files
  # of size >4KiB, therefore, fuzzy hash computed
  # only for files of og greater size
  def compute_fuzzy_hash(self, file):
    file_size_in_bytes = os.path.getsize(file.absolute_path)
    file_size_in_kb = file_size_in_bytes / 1024
    if file_size_in_kb < 4:
      file.delete_fuzzy_hash_entries(file)
    elif file_size_in_kb >= 4:
      file.add_fuzzy_hash(file, ssdeep.hash_from_file(file.absolute_path))

  # This method compares existing and new fuzzy hash
  def compare_fuzzy_hash(self, file):
    # Validation prior to comparesement.
    if len(file.file_fuzzy_hash) > 1:
      return ssdeep.compare(file.file_fuzzy_hash[-2], file.file_fuzzy_hash[-1])
    return None