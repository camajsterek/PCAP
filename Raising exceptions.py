# A program to practice assertions, try and except
# It takes an input and range, then sees if the input is an integer like expected
# and that it is within the valid range

def read_int(prompt, min, max):
    # line 6 to line 22 were the lines I was permitted to modify
    # test the assertion and try to convert the input into an integer
    try:
        val = int(input(prompt))
        assert val > min & val < max
        # return the input if everything is okay
        return val
    # output if a non-integer is entered
    except ValueError:
        print("Error: wrong input.")
        # quit() to stope the program running the print statement below
        quit()
    # output if integer is outside the range
    except AssertionError:
        print("Error: the value is not within the permitted range (",
              min, "..", max, ")", sep="")
        quit()


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
