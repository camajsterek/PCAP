def is_prime(num):
    # since 2 and 3 are special cases
    if num == 2 or num == 3:
        return True
    # no number less than 1 can be prime
    elif num < 1:
        return False
    # actual calculation with the calculation stopping at half the number to save resources
    else:
        # num//2+1, the +1 is needed for 5 otherwise it's discounted due to the range ending at 2
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
            else:
                return True
# I've heard good arguments for 5 being the first actual prime number though since 2 and 3 are clearly special cases.


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
