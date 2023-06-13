#!/usr/bin/python3

""" function that removes all characters c and C from a string """


def no_c(my_string):
    new_string = my_string.translate({ord(x): None for x in "cC"})
    return new_string
