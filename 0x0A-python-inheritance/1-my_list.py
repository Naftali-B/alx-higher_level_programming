#!/usr/bin/python3
"""
1-my_list: MyList
"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Attributes:
        None

    Methods:
        print_sorted(): Prints the list in ascending order.
        sort_list(): Returns the list sorted in ascending order.
    """
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))

    def sort_list(self):
        """Returns the list sorted in ascending order."""
        return sorted(self)

