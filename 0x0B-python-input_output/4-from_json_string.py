#!/usr/bin/python3
""" function that returns a Python object from a JSON string """
import json


def from_json_string(my_str):
    """
        returns an object from a JSON string
        Args:
            my_str: string to be decoded
    """
    return json.loads(my_str)
