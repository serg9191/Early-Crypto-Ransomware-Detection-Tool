import magic

from file import File

class FileType:
  """
  This class implements file type detection, using
  python-magic library.

  Methods
  ---
  determine_file_type()
    This method determines file type. Sets file type to
    this reading. In future, uses this initial file type
    reading as reference point
  compare_file_type()
    This method takes a new reading of the file type.
    Compares new reading against initial reading to detect
    changes.

  """    
  def __init__(self):
    None

  # This method takes file type reading and
  # sets file.file_type to this reading.
  # Method should only be used during detection tool
  # instantiation and new file creation.
  def determine_file_type(self, file):
    if file.file_type != "":
      return
    f = magic.Magic(mime=True)  
    file.set_file_type(file, f.from_file(file.absolute_path))

  # This method compares new file type reading
  # against initial file type reading.
  def compare_file_type(self, file):
    f = magic.Magic(mime=True)  
    new_file_reading = f.from_file(file.absolute_path)
    if file.file_type != new_file_reading:
      if "application/octet-stream" in new_file_reading:
        return True
      file.set_file_type(file, f.from_file(file.absolute_path))
    return False