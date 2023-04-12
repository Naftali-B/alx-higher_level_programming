#!/usr/bin/python3
"""reads file without exceptions"""

def read_file(filename=""):
    """
        reads a text file (UTF-8) and prints to stdout
    """
    with open(filename) as f:
        for line in f:
            print(line, end='')
