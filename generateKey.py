# Import the required module
from cryptography.fernet import Fernet

# Generate the key
key = Fernet.generate_key()

# opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# key generation
key = Fernet.generate_key()

# String the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)