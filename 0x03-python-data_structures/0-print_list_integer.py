#!/usr/bin/python3

""" function that prints all integers of a list """


def print_list_interger(my_list=[]):
    for list_element in range(len(my_list)):
        print("{:d}".format(my_list[list_element]))
