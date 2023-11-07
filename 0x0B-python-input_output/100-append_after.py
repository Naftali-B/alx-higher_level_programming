#!/usr/bin/python3
"""  inserts a line of text to a file,
    after each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The text to be inserted.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
