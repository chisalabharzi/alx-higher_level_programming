#!/usr/bin/python3
""" class rectangle that defines a rectangle """


class rectangle:
    """ define a new class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes the attributes w & h with default value 0 """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the vale of width """
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
        """ retrives the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(" height must be an integer ")
        if value < 0:
            raise ValueError(" height must be >= 0 ")
        self.__height = value

    def area(self):
        """ area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ return readable representation of rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ return string that rep expression of the rectangle """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del(self):
        """ object about to be destroyed """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
