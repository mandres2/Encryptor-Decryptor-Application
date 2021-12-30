# Encryptor-Decryptor-Application

### General Overview of the Application

The program was written in Python to encrypt and decrypt user uploaded files.

<hr/>

### Concepts

#### What is Encryption?

It is a series of steps of converting information into some form of code to hide its true content or the process of converting plain text to cipher text. Encryption is also called encoding and the only way to access the file information is to decrypt it.

#### What is Decryption?

The process of converting cipher text to plain text is called decryption. It is also coined as decoding


#### What is Cryptography?

Cryptography is the study of secure communications techniques that allow the sender and intended recipient of a message to view its contents. The term is derived from the Greek word <i>kryptos</i>, which means hidden. It is closely associated to encryption and decryption.

* In this application the Python cryptography module will be used.

Cryptography is a python package used for the encryption or decryption of files such as text file, document file, csv file, python file etc.

Here we will be using cryptography’s fernet module to generate the encryption key and encrypt the file using encrypt() method.

The encryption of file converts the file's content into cipher text which can be decrypted only by using the same encryption key.

<hr/>

### Tools

* Updated Text-Editor or IDE
    * Any VS Code version higher than: 1.63.1
    * Any PyCharm version higher than: Version: 2021.3.1
        * Build: 213.6461.77
* Python v3.10+
* Any version higher than: pip 21.3.1

* cryptography
    * Installation 01: ```pip install cryptography```
    * Installation 02: ```pip install Fernet```

<hr/>

## Encrypt.py

### Understanding the Encrypt Code:

After importing the dependencies generate the key using ```generate_key()``` method.
```py
key = Fernet.generate_key()
```
Save the key in file_key.key file.
```py
with open('file_key.key', 'wb') as filekey:
        filekey.write(key)
```
Load the generated key with instance of Fernet class.
```py
fernet = Fernet(key)
```
Read the file that you want to encrypt.
```py
with open('test.txt', 'rb') as f:
        file = f.read()
```
Encrypt the file using encrypt() method.
```py
encrypt_file = fernet.encrypt(file)
```
Rewrite the file with encrypted data.
```py
with open('your_uploadedFile.ext', 'wb') as encrypted_file:
        encrypted_file.write(encrypt_file)```
```

<hr/>

## Decrypt.py

### Understanding the Decrypt Code:

```py
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
```