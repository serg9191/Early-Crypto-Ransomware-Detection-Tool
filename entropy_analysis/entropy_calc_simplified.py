import json
import math
import os 
import sys
import shutil

from encrypt        import AesEncrypt
from url_downloader import UrlDownloader
from url_finder     import UrlFinder

def main():
  # A list of extension to be tested
  file_extensions = ['docx', 'txt', 'pdf']
  # Number of test files per extension
  number_of_test_file = 5

  # Initialise class AesEncrypt and store in variable
  # aes_encryptor
  aes_encryptor = AesEncrypt()

  # Create two directories: before and after encryption that will
  # store corresponding files
  before_encryption_dir_name = "entropies/before_encryption"
  create_folder(before_encryption_dir_name)
  after_encryption_dir_name = "entropies/after_encryption"
  create_folder(after_encryption_dir_name)  

  # The outer loop that implements url_finder and url_downloader:
  # Iterates over every file extension, finds urls and
  # downloads number of specified test files from these urls
  for extension in file_extensions:
    url_finder = UrlFinder(extension, number_of_test_file)
    url_finder.query_search_engine()
    url_downloader = UrlDownloader(url_finder)
    url_downloader.start_download()
    download_dir_path = url_downloader.path_to_download_dir
    # Two variables that keep track of entropies and later
    # produce average calculation.
    avg_entropy = 0
    avg_entropy_after_encryption = 0

    # Inner loop that perform entropy calculation per every downloaded file;
    # Also encrypts the file, and performs entropy calculation once more.
    for root, dirs, files in os.walk(download_dir_path):
      for file in files:
        path_to_file = os.path.join(root, file)
        # Flag variable to determine type of file, encrypted or not.
        aes = False
        avg_entropy += entropy_processes_as_one(url_finder, path_to_file, aes, before_encryption_dir_name)
        file_in = path_to_file
        file_out = file_in + ".aes"
        aes_encryptor.encrypt_file(file_in, file_out)
        aes = True
        avg_entropy_after_encryption += entropy_processes_as_one(url_finder, file_out, aes, after_encryption_dir_name)

    # Find average of all entropies
    avg_entropy = find_average_entropy(avg_entropy, url_finder)
    avg_entropy_after_encryption = find_average_entropy(avg_entropy_after_encryption, url_finder)
    # Form valid json format of average entropies and append to the file
    json_avg_entropy = {'avg_entropy': avg_entropy}
    json_avg_entropy_after_encryption = {'avg_entropy_after_encryption': avg_entropy_after_encryption}
    write_json_to_file(None, url_finder.extension, json_avg_entropy, before_encryption_dir_name)
    write_json_to_file(None, url_finder.extension  + ".aes", json_avg_entropy_after_encryption, after_encryption_dir_name)


# This method creates folder under the specified path
def create_folder(folder_name):
  # Set variable value to current dir along with extensions in question
  output_dir = folder_name
  # Try block to clear content of the download folder.
  # May throw exception if does not exist
  try:
    shutil.rmtree(output_dir)
  except:
     print("exception in " + output_dir +  """  during the attempt to
      delete dir content, probably does not exist""")
  # Create folder under the given path, even if it already exists
  os.makedirs(output_dir, exist_ok = True)

# This function is a sum of functions that derives file entropy
def entropy_processes_as_one(url_finder, path_to_file, aes, directory):
  file_as_byte_array = read_file(path_to_file)
  file_size = find_file_size(file_as_byte_array)
  frequency_list = calculate_frequency_of_bytes(file_as_byte_array, file_size)
  frequency_as_json = format_frequency_list_as_json(frequency_list)
  entropy = calculate_entropy(frequency_list)
  json_formatted = form_final_output_as_json(frequency_as_json, file_size,
                    path_to_file, entropy)
  if aes:
    write_json_to_file(json_formatted, url_finder.extension + ".aes", None, directory)
  else:    
    write_json_to_file(json_formatted, url_finder.extension, None, directory)
  print(entropy)
  return entropy

# This method return average of numbers
def find_average_entropy(avg_entropy, url_finder):
  return avg_entropy / url_finder.num_of_results

# This method creates a file and write some data into it
def compose_file(path_to_file):
  with open(path_to_file,"a+") as file:
    file.write("abcd")  

# This method writes formatted json object into the file
def write_json_to_file(json_formatted, extension, avg_entropy, directory):
  file_name = os.path.join(directory, ('entropy_' + extension + '.json'))
  if not avg_entropy:
    with open(file_name, 'a+', encoding='utf-8') as file:
      json.dump(json_formatted, file, indent=4, sort_keys=True)
  else:
    with open(file_name, 'a+', encoding='utf-8') as file:
      json.dump(avg_entropy, file, indent=4, sort_keys=True)    


# This method forms json object from the given arguments
def form_final_output_as_json(frequency_as_json, file_size,
                                    path_to_file, entropy):
  return {
    'frequency': frequency_as_json,
    'file_size': file_size,
    'file_path': path_to_file,
    'entropy'  : entropy
  }

# This method forms list of frequency into
# nicely formatted, readable json object
def format_frequency_list_as_json(frequency_list):
  frequency_as_json = {}
  for i in range(0, len(frequency_list)):
    frequency_as_json[str(chr(i).encode('utf-8'))] = frequency_list[i]
  return frequency_as_json

# This method responsible for entropy calculation derived from
# frequency list
def calculate_entropy(frequency_list):
  entropy = 0.0
  if not frequency_list:
    return entropy
  else:
    for frequency in frequency_list: 
      if frequency > 0: 
        entropy = entropy + frequency * math.log(frequency, 2)
    return -entropy     

# This method reads file from given src and parses it into byte array
def read_file(path_to_file):
  file_size = os.path.getsize(path_to_file)
  f = open(path_to_file, 'rb')
  file_as_byte_array = bytearray(f.read(file_size))
  f.close()
  return file_as_byte_array

# This method returns size of the file/byte-array
def find_file_size(file_as_byte_array):
  return len(file_as_byte_array)

# This method calculates frequency of the bytes in the byte-array
def calculate_frequency_of_bytes(file_as_byte_array, file_size):
  # Empty file validation
  if file_size <= 0:
    return []
  else:   
    frequency_list = []
    all_ascii_characters = 256
    # Outer loop that iterates via each ascii character,
    # a total of 256
    for ascii_character in range(all_ascii_characters):
      frequency_counter = 0 
      # Inner loop that calculates frequency, apperance of the
      # ascii character in the file
      for byte in file_as_byte_array: 
        if byte == ascii_character:
          frequency_counter += 1
      # Frequency determined via product of division of char frequency
      # over file size and stored in the list 
      frequency_list.append(float(frequency_counter) / file_size)
  return frequency_list

if __name__== "__main__":
  main()