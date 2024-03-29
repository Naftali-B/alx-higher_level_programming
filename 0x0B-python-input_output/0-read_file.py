#!/usr/bin/python3
""" a function that reads a text file (UTF8)
    and prints it to stdout: """


def read_file(filename=""):
    """
        input: text file
        uses with statement
        so python closes the file automatically
    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
