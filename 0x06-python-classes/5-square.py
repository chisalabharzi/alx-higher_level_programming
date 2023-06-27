#!/usr/bin/python3
""" class Square """


class Square:
    """ define a square """
    def __init__(self, size):
        """ new square initialization.
        args:
        size (int): new square size.
        """
        self.size = size

    @property
    def size(self):
        """ set current square size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError(" size must be an integer ")
        elif value < 0:
            raise ValueError(" size must be >= 0 ")
        self.__size = value

    def area(self):
        """ return curent square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ print Square with # character """
        for k in range(0, self._size):
            [print("#", end="") for j in range(self.__size)]
            print("")
            if self.__size == 0:
                print("")
