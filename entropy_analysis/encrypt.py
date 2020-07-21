import pyAesCrypt


# This class is not unit tested as it only
# uses already existing python library.
class AesEncrypt():
  """
  A class that implements aes encryption using
  python library pyAesCrypt 0.4.3

  Attributes
  ---
  buffer_size : int
    a variable to indicate size of buffer
  password : str
    key for encryption and decryption

  Methods
  ---
  ecrypt_file()
    encrypts file that is specified by the
    arg file_in and outputs encryption result
    as arg file_out.
  """  
  def __init__(self):      
    self.buffer_size = 64 * 1024
    self.password = "password"

  # A method that encrypts file using aes encryption 
  def encrypt_file(self, file_in, file_out):
    with open(file_in, "rb") as f_in:
      with open(file_out, "wb") as f_out:
        pyAesCrypt.encryptStream(f_in, f_out, self.password, self.buffer_size)