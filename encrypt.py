from cryptography.fernet import Fernet

print("Note: The file must be uploaded within this application repository prior to running the program to pick up the file and encrypt it")
fileName = input("Please enter the name of the file you want to encrypt (Must include file extension - i.e. 'sample.sql'): ")

key = Fernet.generate_key()
with open('file_key.key', 'wb') as filekey:
    filekey.write(key)
fernet = Fernet(key)
with open(fileName, 'rb') as f:
    file = f.read()

encrypt_file = fernet.encrypt(file)
with open(fileName, 'wb') as encrypted_file:
    encrypted_file.write(encrypt_file)
print('File is encrypted. Please double check that the file is encrypted and do not run the program again, because it will overwrite the encrypted file.')