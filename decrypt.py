from cryptography.fernet import Fernet

print("Note: The file must be uploaded within this application repository prior to running the program to pick up the file and decrypt it")
fileName = input("Please enter the name of the file you want to decrypt (Must include file extension - i.e. 'sample.sql'): ")

# read the key
with open('file_key.key', 'rb') as filekey:
    key = filekey.read()
# crate instance of Fernet
# with encryption key
fernet = Fernet(key)
# read the file to decrypt
with open(fileName, 'rb') as f:
    file = f.read()

# decrypt the file
decrypt_file = fernet.decrypt(file)
# open the file and wite the encrypted data
with open(fileName, 'wb') as decrypted_file:
    decrypted_file.write(decrypt_file)
print('File is decrypted')