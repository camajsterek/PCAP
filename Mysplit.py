# recreating the split() method with my own function

def mysplit(strng):
    output = [""]
    i = 0
    for ch in strng:
        if ch == " ":
            output += " "
        else:
            output[-1] += ch
    for ln in range(len(output)):
        output[ln] = output[ln].strip()
    while i < len(output):
        if output[i] == "":
            del output[i]
        else:
            i += 1
    return output


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
