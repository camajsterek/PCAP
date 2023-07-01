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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1.getx(), vertice1.gety(), vertice2.getx(
        ), vertice2.gety(), vertice3.getx(), vertice3.gety()]

    def perimeter(self):
        self.__peri = math.hypot(self.__points[0]-self.__points[2], self.__points[1]-self.__points[3]) + math.hypot(
            self.__points[2]-self.__points[4], self.__points[3]-self.__points[5]) + math.hypot(self.__points[4]-self.__points[0], self.__points[5]-self.__points[1])
        return self.__peri


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
