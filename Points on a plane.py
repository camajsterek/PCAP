# Yet another lab on classes

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        # container for coordinates
        self.__coord = [x, y]

    # getter for x
    def getx(self):
        return self.__coord[0]

    # getter for y
    def gety(self):
        return self.__coord[1]

    def distance_from_xy(self, x, y):
        return math.hypot(self.__coord[0]-x, self.__coord[1]-y)

    def distance_from_point(self, point):
        return math.hypot(self.__coord[0]-point.getx(), self.__coord[1] - point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
