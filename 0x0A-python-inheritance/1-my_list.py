#!/usr/bin/env/python3
"""class MyList that inherits from list"""


class MyList(list):
    """
        Public instance method:
            def print_sorted(self):
            that prints the list,
            but sorted (ascending sort)

        You can assume that all the elements of the list will be of type int
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

