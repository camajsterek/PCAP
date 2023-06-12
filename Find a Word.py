# A program that takes a string and then finds if all the characters are within a second string, in order.

# Get the inputs
target = input("Please type the target word: ").lower()
sample = input("Please type the sample text: ").lower()

# create iterators, i for the target length and a for indexing the sample
i = 0
a = 0

# compare the target to the sample, if find returns -1, break.
# increase the size of a to match the last found version of that letter
while i < (len(target)):
    if int(sample.find(target[i], a)) < 0:
        print("Target word not found.")
        break
    if a < i:
        a = i+1
    else:
        a = sample.find(target[i], a)
    i += 1

# Output on success
if i == len(target):
    print("The target word is hidden in the sample.")
