#!/usr/bin/python3
""" a function that returns the dictionary  """


def class_to_json(obj):
    """
        obj is an instance of a Class
    """
    return obj.__dict__
