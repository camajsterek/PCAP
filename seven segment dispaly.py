# A program to take a list of digits and convert them into a seven segment display
# limitations are that only the digits 0-9 can be entered

# create the output variables
one = ("  #", "  #", "  #", "  #", "  #")
two = ("###", "  #", "###", "#  ", "###")
three = ("###", "  #", "###", "  #", "###")
four = ("# #", "# #", "###", "  #", "  #")
five = ("###", "#  ", "###", "  #", "###")
six = ("###", "#  ", "###", "# #", "###")
seven = ("###", "  #", "  #", "  #", "  #")
eight = ("###", "# #", "###", "# #", "###")
nine = ("###", "# #", "###", "  #", "###")
zero = ("###", "# #", "# #", "# #", "###")

# create dictionary to convert from input to output variables
conversion = {
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
    "0": zero
}

# define display function


def display(user):
    # changes input into separated list of values
    transform = list(user)
    # uses the dictionary to swap from digits in string form to the words in the dictionary, words required due to variable naming
    for i in range(len(transform)):
        transform[i] = conversion[transform[i]]
    # iterates over the 5 lines of the display, with an inner iteration over each line of the numbers
    for k in range(5):
        for j in range(len(transform)):
            print(transform[j][k], end=" ")
        # empty print is just a hack to create a new line at the end of the j iteration
        print("")


# get input
user = input("please enter a number to display: ")

# run function
display(user)
