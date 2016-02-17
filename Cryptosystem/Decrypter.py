# This is the decrypter which decrypts words encrypted in the Encrypter.py file
word = raw_input("Let's decrypt a string! Enter encrypted string for decryption: ")

# Cipher holds the corresponding value of the decrypted letter
cipher = []

# looping through the encrypted string and returning corresponding letters if found
for letter in word:
    if letter == " ":
        cipher.append(" ")
    if letter == "b":
        cipher.append("a")
    if letter == "e":
        cipher.append("b")
    if letter == "a":
        cipher.append("c")
    if letter == "v":
        cipher.append("d")
    if letter == "t":
        cipher.append("e")
    if letter == "d":
        cipher.append("f")
    if letter == "x":
        cipher.append("g")
    if letter == "o":
        cipher.append("h")
    if letter == "h":
        cipher.append("i")
    if letter == "s":
        cipher.append("j")
    if letter == "q":
        cipher.append("k")
    if letter == "y":
        cipher.append("l")
    if letter == "g":
        cipher.append("m")
    if letter == "l":
        cipher.append("n")
    if letter == "j":
        cipher.append("o")
    if letter == "m":
        cipher.append("p")
    if letter == "f":
        cipher.append("q")
    if letter == "i":
        cipher.append("r")
    if letter == "c":
        cipher.append("s")
    if letter == "n":
        cipher.append("t")
    if letter == "k":
        cipher.append("u")
    if letter == "u":
        cipher.append("v")
    if letter == "z":
        cipher.append("w")
    if letter == "r":
        cipher.append("x")
    if letter == "l":
        cipher.append("y")
    if letter == "p":
        cipher.append("z")


# Printing out the decrypted string
print "Your encrypted message has been successfully decrypted. It reads: %s" % (''.join(cipher))
