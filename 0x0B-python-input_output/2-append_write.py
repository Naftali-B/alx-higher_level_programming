#!/usr/bin/python3
""" a function that appends a string at the end of a text file
     and returns the number of characters """


def append_write(filename="", text=""):
    """"If the file doesn’t exist, it should be created
        must use the with statement
        Args: filename, text
        encoding: utf-8
        returns the number of characters added:
    """"

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
