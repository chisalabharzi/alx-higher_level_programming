#!/usr/bin/python3
""" class rectangle that defines a rectangle in task 2 """


class Rectangle:
    """ define a new class """

    def __init__(self, width=0, height=0):
        """ initializes attributes w & h with default value 0 """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(" width must be an integer ")
        if value < 0:
            raise ValueError(" width must be >= 0 ")
        self.__width = value

    @property
    def height(self):
        """ gets th value of height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(" height must be an integer ")
        if value < 0:
            raise ValueError(" hight must be >= 0 ")
        self.__height = value

    def area(self):
        """ area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ return readable represanttion of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
