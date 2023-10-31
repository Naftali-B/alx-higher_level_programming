#!/usr/bin/python3
""" adds two integers """

def add_integer(a, b=98):

    """
        adds two integers
        Args:
            a: first int or float
            b: second int or float (optional since a default is provided(98))
        Returns:
            int: the sum of a and b

    """
    if type(a) not in [int, float] or a is None:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float] or b is None:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
