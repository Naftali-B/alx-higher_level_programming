#!/usr/bin/python3
""" a class Square that inherits from (9-rectangle.py) """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class Square extends class Rectangle
    """

    def __init__(self, size):
        """
            initializes all instances of Square
            Args:
                size(int): size of the square
        """

        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
            returns area of Square
        """

        return self.__size ** 2
