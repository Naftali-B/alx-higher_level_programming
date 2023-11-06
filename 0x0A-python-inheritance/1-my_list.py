#!/usr/bin/python3
""" My_list: MyList """

class List(self):
	pass

class MyList(list):
    """
        class MyList
        that inherits from list
        Methods:
            print_sorted: prints sorted list
    """
    def print_sorted(self):
        """
            prints list sorted in ascending order
        """
        print(sorted(self))
