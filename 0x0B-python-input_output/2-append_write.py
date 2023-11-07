#!/usr/bin/python3
""" function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """
        takes filename and text string
        appends the string to end of a text file (UTF8)
        Return:
            no of characters added
    """

    with open(filename, 'a+') as file:
        file.write(text)
    return len(text)
