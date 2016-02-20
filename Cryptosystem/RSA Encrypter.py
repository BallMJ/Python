"""--RSA txt file Encrypter and decrypter using pycrypto--
-Code is a bit messy at the moment (quite raw and far from
 what I am aiming for), updates are coming

-More additions will be made to this code including:
 Generating files as per user input request
 seperating encryption and decryption into seperate functions
"""

#importing all packages/modules needed
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import sys

# user input of filename and encryption strength
print "--WELCOME TO THE RSA ENCRYPTER AND DECRYPTER--"
filename = raw_input("Name of file you want to encrypt: ")
strength = int(raw_input("How strong do you want the encryption: "))

# Assigning variables for RSA number and public key
rand = Random.new().read
key = RSA.generate(strength, rand)
pubkey = key.publickey()

# Open files to read and write
x = open(filename, "r")
y = open("encryptionRSA.txt", "w")

# RSA Encryption process
with x as inp:
    data = str(list(inp))
    encrypted = pubkey.encrypt(data, 32)
    print >>y, encrypted
    y.close()
    print "--RSA ENCRYPTION COMPLETE--"
    print "Encrypted message saved in 'encryptionRSA.txt'"


# Open files for read and write
t = open("encrypttest.txt", "r")
b = open("decryptionRSA.txt", "w")

# RSA Decryption process
message = t.read()
decrypter = key.decrypt(ast.literal_eval(str(encrypted)))

print >>b, "Your decrypted file message is: %s" % (decrypter), '\n', message
t.close()
b.close()
print "--RSA DECRYPTION COMPLETE--"
print "Decrypted message saved in 'decryptionRSA.txt'"



