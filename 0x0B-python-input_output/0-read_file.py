#!/usr/bin/python3


def read_file(filename=""):
    """define function that reads text-file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
