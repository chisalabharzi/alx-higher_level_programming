#!/usr/bin/python3
""" class Rectangle that defines a rectangle based on task 0 """


class Rectangle():
    """ Initialize a new rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """ retrive value for height """
        return (self.__height)

    @property
    def width(self):
        """ retrive value for width """
        return (self.__width)

    @height.setter
    def height(self, value):
        """ checks and sets the height value """
        if not isinstance(value, int):
            raise TypeError(" height must be an integer ")
        elif value < 0:
            raise ValueError(" height must be >= 0 ")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """ checks and sets the width value """
        if not isinstance(value, int):
            raise TypeError(" width must be an integer ")
        elif value < 0:
            raise ValueError(" width must be >= 0 ")
        else:
            self.__width = value
