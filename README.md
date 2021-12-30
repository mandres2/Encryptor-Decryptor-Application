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
    * Installation: ```pip install cryptography```
    * Installation 02: ```pip install Fernet```