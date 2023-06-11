# A Plaindrome checker that takes an input, strips it of case, numbers and punctuation.

# Get user input
entry = input("Please enter a phrase to test: ").lower()
palin = ""

# Strip of non-letters
for char in entry:
    if not char.isalpha():
        continue
    else:
        palin += char

# Reverse the phrase
nilap = palin[::-1]

# Preform the check
if nilap == palin:
    print("It's a palindrome!")
else:
    print("It is NOT a palindrome!")
