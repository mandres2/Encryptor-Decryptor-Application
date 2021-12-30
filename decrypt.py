from cryptography.fernet import Fernet

print("Note: Check that the file was uploaded within this application repository prior to running the program to pick up the file and decrypt it")
fileName = input("Please enter the name of the file you want to decrypt (Must include file extension - i.e. 'sample.sql'): ")

with open('file_key.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)
with open(fileName, 'rb') as f:
    file = f.read()

decrypt_file = fernet.decrypt(file)
with open(fileName, 'wb') as decrypted_file:
    decrypted_file.write(decrypt_file)
print('File is decrypted')