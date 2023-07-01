# Yet another lab, this time looking at incrementing days of the week.

class WeekDayError(Exception):
    pass


class Weeker:
    # Create a tuple for indexing the days of the week
    __tpl = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        # Try statement to raise the excpetion if incorrect data is entered
        try:
            self.__dy = self.__tpl.index(day)
        except:
            raise WeekDayError

    # a method to return the day based on the current number
    def __str__(self):
        return self.__tpl[self.__dy]

    # a method for increasing a set number of days
    def add_days(self, n):
        self.__dy += n % 7
        # %= 7 returns the number to the range of __tpl
        self.__dy %= 7

    # a method for decreasing a set number of days
    def subtract_days(self, n):
        # using the remainder to decrement, ensures the number doesn't end up beyond -7 and thus outside the range of the reseting +7
        self.__dy -= n % 7
        if self.__dy < 0:
            self.__dy += 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
