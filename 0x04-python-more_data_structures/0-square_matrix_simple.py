#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_list = []
    if len(matrix) == 0:
        return new_list
    new_list = [[x*x for x in y] for y in matrix]
    return new_list
