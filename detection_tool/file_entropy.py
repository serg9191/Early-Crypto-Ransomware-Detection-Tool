import os
import math
import time
import textwrap
import calendar

class FileEntropy():
  """
  A class to represent file entropy.
  In addition, to produce entropy computation
  and byte frequency.
  Attributes
  ---
  file_as_byte_array: list
    a list to contain search results
  file_size: int
    a correctly formed query for search
  entropy: float
    the extension in question
  frequency_list: list
    the number of desired search results
  time_when_entropy_measured: integer
    the number of desired search results    

  Methods
  ---
  calculate_frequency_of_bytes()
    This method calculates the number of
    byte occurrence in the file
  calculate_file_entropy()
    This method performs entropy calculation
    based on the values of the file frequency
    list. Entropy measured in range 0 to 8.
  print_when_entropy_was_measured(url)
    This method prints when entropy was measure.
  to_string()
    This method return textual representation of
    the object.
  """  
  def __init__(self, file_as_byte_array, file_size):
    """
    Parameters
    ----------
    file_as_byte_array : list
      The list containing byte frequency
    file_size : int
      The file size               
    """        
    self.file_as_byte_array         = file_as_byte_array
    self.file_size                  = file_size
    self.entropy                    = 0.0
    self.frequency_list             = []
    self.time_when_entropy_measured = 0


  # Author: Kenneth G. Hartman
  # Source: https://kennethghartman.com/calculate-file-entropy/
  # This method calculates frequency of the bytes in the byte-array
  def calculate_frequency_of_bytes(self):
    self.frequency_list = []
    all_ascii_characters = 256
    # Outer loop that iterates via each ascii character,
    # a total of 256    
    for ascii_character in range(all_ascii_characters):
      frequency_counter = 0 
      # Inner loop that calculates frequency, apperance of the
      # ascii character in the file      
      for byte in self.file_as_byte_array: 
        if byte == ascii_character:
          frequency_counter += 1 
      try:
          # Frequency determined via product of division of char frequency
          # over file size and stored in the list         
          self.frequency_list.append(float(frequency_counter) / self.file_size)
      except ZeroDivisionError:
          pass                


  # Author: Kenneth G. Hartman
  # Source: https://kennethghartman.com/calculate-file-entropy/      
  # This method responsible for entropy calculation derived from
  # frequency list
  def calculate_file_entropy(self):
    for frequency in self.frequency_list: 
        if frequency > 0: 
            self.entropy = self.entropy + frequency * math.log(frequency, 2)
    self.entropy = -self.entropy
    self.time_when_entropy_measured = calendar.timegm(time.gmtime())

  # This method prints when was entropy measure in time
  def print_when_entropy_was_measured(self):
    print(time.strftime('%m/%d/%Y %H:%M:%S',  time.localtime(self.time_when_entropy_measured)))

  # This method return formatted textual representation
  # of the object, entropy.
  def to_string(self):
    return textwrap.dedent(
      """\
      entropy: {0}
      """.format(
        self.entropy))