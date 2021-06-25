from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
    #Output: will create a file called mykey.key with a string of mixed letters and numbers