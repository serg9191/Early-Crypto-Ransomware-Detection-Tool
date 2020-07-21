import pywintypes
import win32api

class DriveFinder:
  """
  A class used to perform device drive lookup

  Attributes
  ---
  list_of_all_drive: list
    A list to store found device drives

  Methods
  ---
  identify_device_drives()
    this method calls win32api library and stores
    the output in the list_of_all_drives
    variable.
  normalize_device_drive_output()
    This method splits string containing
    all device drives and each split value append
    into the list.
  get_all_device_drives()
    This method returns list_of_all_drives
  """
  def __init__(self, list_of_all_drives):
    """
    Parameters
    ----------
    list_of_all_drives : list
      Takes list of all drives.
    """    
    self.list_of_all_drives = list_of_all_drives

  # This method find the device drives
  def identify_device_drives(self):
    # Find all device drives
    self.list_of_all_drives = win32api.GetLogicalDriveStrings()

  # This method splits single string and allocates each
  # splitted value to the list
  def normalize_device_drive_output(self):
    # Normalize data convention to standard form i.e. C://
    self.list_of_all_drives = self.list_of_all_drives.split('\000')[:-1]

  # This method returns list_of_all_drives
  def get_all_device_drives(self):
    return self.list_of_all_drives

