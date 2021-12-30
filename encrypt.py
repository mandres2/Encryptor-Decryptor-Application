from cryptography.fernet import Fernet

print("Note: The file must be uploaded within this application repository prior to running the program to pick up the file and encrypt it")
fileName = input("Please enter the name of the file you want to encrypt (Must include file extension - i.e. 'sample.sql'): ")

# generate encryption key
key = Fernet.generate_key()
# write the key in a file of .key extension
with open('file_key.key', 'wb') as filekey:
    filekey.write(key)
# crate instance of Fernet
# and load generated key
fernet = Fernet(key)
# read the file to encrypt
with open(fileName, 'rb') as f:
    file = f.read()

# encrypt the file
encrypt_file = fernet.encrypt(file)
# open the file and wite the encryption data
with open(fileName, 'wb') as encrypted_file:
    encrypted_file.write(encrypt_file)
print('File is encrypted. Please double check that the file is encrypted and do not run the program again, because it will overwrite the encrypted file.')