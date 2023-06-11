# A program to take the numerals of one's birth and return a single "digit of life".

# get user input and strip any spaces
dateOfBirth = str(
    input("Please enter your date of birth using digits only, include the whole year: ").replace(" ", ""))

# create the adder function


def Adder(dateOfBirth):
    beep = 0
    for char in range(len(dateOfBirth)):
        beep += int(dateOfBirth[char])
    return beep


# run the adder function
digitOfLife = Adder(dateOfBirth)

# if you don't get a single digit, rerun the adder
while digitOfLife > 9:
    digitOfLife = Adder(str(digitOfLife))

# output the result
print("Your digit of life is: ", digitOfLife)
