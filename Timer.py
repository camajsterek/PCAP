# A short program exploring classes further.  This creates a timer class that counts seconds and formats it in HHMMSS

class Timer:
    # Initialise the class with three variables
    def __init__(self, HH, MM, SS):
        self.__time = [HH, MM, SS]

    # format the output with preceding 0 using if/else statements.  I'm certain there's efficiency to be found here but oh well.
    # the instructions did indicate I should do this with a function but the code outline included this method so 🤷
    def __str__(self):
        if self.__time[0] < 10:
            self.__str1 = "0" + str(self.__time[0])
        else:
            self.__str1 = str(self.__time[0])
        if self.__time[1] < 10:
            self.__str2 = "0" + str(self.__time[1])
        else:
            self.__str2 = str(self.__time[1])
        if self.__time[2] < 10:
            self.__str3 = "0" + str(self.__time[2])
        else:
            self.__str3 = str(self.__time[2])
        return self.__str1 + ":" + self.__str2 + ":" + self.__str3

    # a method to incriment a second and cascade up through the time.
    def next_second(self):
        if self.__time[2] < 59:
            self.__time[2] += 1
        elif self.__time[1] == 59:
            self.__time[1] += 1
            self.__time[2] = 0
            if self.__time[1] == 60:
                self.__time[0] += 1
                self.__time[1] = 0
                if self.__time[0] == 24:
                    self.__time[0] = 0

    # a method to decrement a second!
    def prev_second(self):
        if self.__time[2] > 0:
            self.__time[2] -= 1
        elif self.__time[2] == 0:
            self.__time[1] -= 1
            self.__time[2] = 59
            if self.__time[1] == -1:
                self.__time[0] -= 1
                self.__time[1] = 59
                if self.__time[0] == -1:
                    self.__time[0] = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
