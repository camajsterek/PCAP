# A program to check whether two inputs are anagrams or not.
# Punctuation is a limitation, including it results in looking to see if both contain the same punctuation

# get the users inputs, make it all lowercase, strip the white space and sort into a list
sample1 = sorted(input("Please enter the first sample text without punctuation: ").lower().replace(
    " ", ""))
sample2 = sorted(input("Please enter the second sample text without punctuation: ").lower().replace(
    " ", ""))

# check the input wasn't empty
if (sample1 == [] or sample2 == []):
    print("Emptiness is not an anagram")

# compare to see if the same letters were included in the same frequency
elif sample1 == sample2:
    print("They are anagrams!")
else:
    print("Not anagrams")
