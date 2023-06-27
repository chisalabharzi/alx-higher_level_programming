#!/usr/bin/python3
""" cass Square """


class Square:
    """ define a square """
    def __init__(self, size=0):
        """ Initialize a new square from class
        args:
            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError(" size must be an integer ")
        elif size < 0:
            raise ValueError(" size must be >= 0 ")
        self .__size = size

    def area(self):
        """ return area of the square """
        return (self .__size * self .__size)
