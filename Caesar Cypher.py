# A program that takes a users input and shifts the english letters by the corresponding cipher input.
# Numbers, case and spaces are preserved, non-english characters may display unusual properties.

# Take user input for both the message and encryption factor.
text = input("Please enter your message to be encrypted: ")


def shift():
    fact = int(input("Please enter an encryption factor between 1 and 25: "))
    while (fact > 25 or fact < 1):
        fact = int(input("Stop being naughty, between 1 and 25: "))
    return fact


# store the shift factor in a variable
shift = shift()

# create output variable
cypher = ""

# run the encryption
for char in text:
    # skips non letter characters
    if not char.isalpha():
        cypher += char
    code = ord(char) + shift
    # upper and lower check to preserve integrity of upper and lower, -26 for runover issues.
    if char.isupper():
        if code > ord("Z"):
            code -= 26
        cypher += chr(code)
    if char.islower():
        if code > ord("z"):
            code -= 26
        cypher += chr(code)

print(cypher)
