# This is a simple word/sentence random letter ecrypter 
print "Welcome to this simple word encrypter"
print ""

# assigning variables
word = raw_input("Pick a word or sentence to be encrypted: ")
cipher = []

# sifting through each letter and appending the encrypted value to the cipher variable
for letter in word:
    if letter == " ":
        cipher.append(" ")
    if letter == "a":
        cipher.append("b")
    if letter == "b":
        cipher.append("e")
    if letter == "c":
        cipher.append("a")
    if letter == "d":
        cipher.append("v")
    if letter == "e":
        cipher.append("t")
    if letter == "f":
        cipher.append("d")
    if letter == "g":
        cipher.append("x")
    if letter == "h":
        cipher.append("o")
    if letter == "i":
        cipher.append("h")
    if letter == "j":
        cipher.append("s")
    if letter == "k":
        cipher.append("q")
    if letter == "l":
        cipher.append("y")
    if letter == "m":
        cipher.append("g")
    if letter == "n":
        cipher.append("l")
    if letter == "o":
        cipher.append("j")
    if letter == "p":
        cipher.append("m")
    if letter == "q":
        cipher.append("f")
    if letter == "r":
        cipher.append("i")
    if letter == "s":
        cipher.append("c")
    if letter == "t":
        cipher.append("n")
    if letter == "u":
        cipher.append("k")
    if letter == "v":
        cipher.append("u")
    if letter == "w":
        cipher.append("z")
    if letter == "x":
        cipher.append("r")
    if letter == "y":
        cipher.append("l")
    if letter == "z":
        cipher.append("p")
    
# printing out the encrypted word/sentence
print "This is your encrypted word: %s" % (''.join(cipher))
