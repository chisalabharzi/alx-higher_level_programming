#!/usr/bin/python3

""" function that prints integers in reverse """


def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()

        for x in range(len(my_list)):
            print("{:d}".format(my_list[x]))
