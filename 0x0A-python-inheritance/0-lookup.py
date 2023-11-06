#!/usr/bin/python3
""" function that returns the list of available attributes and methods of obj """


def lookup(obj):
    """
        Returns the list of available attributes and methods of obj
        Args:
            obj: the object we are checking attributes and methods
        Return:
            the list of attributes and methods
    """
    return dir(obj)
