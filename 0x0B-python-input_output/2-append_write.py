#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added.
    If the file doesn't exist, it will be created.
    Args:
        filename (str): The name of the file.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
