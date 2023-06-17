# A program to check whether a sudoku is solved or not
import sys
allData = [input("Please enter a line: ") for i in range(9)]
comparison = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Test to see if 1-9 is present in each row
for i in range(9):
    if sorted(allData[i]) != comparison:
        print("Row test failed, issue in row ", i+1, ".", sep="")


# Test to see if 1-9 is present in each column
for i in range(9):
    column = [j[i] for j in allData]
    if sorted(column) != comparison:
        print("Column test failed, issue in column ", i+1, ".", sep="")

# Test to see if the tiles contain 1-9
z = 0
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        z += 1
        til = [[allData[k+i][l+j] for l in range(3)] for k in range(3)]
        es = [x for y in til for x in y]
        if sorted(es) != comparison:
            print("Tile test failed, issue in Tile", z, ".")

# I'll be honest, this is likely buggy and I hate it.  List comprehensions melt my brain as it is.
# The tile list comprehension was horrific for me.  I'm sure there's a far better way to do this and
# I definitely don't think the PCAP provided enough test data for this lab to thoroughly test it.
# I hope never to set eyes on this again.
