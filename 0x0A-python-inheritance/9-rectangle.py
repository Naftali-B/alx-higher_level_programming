#!/usr/bin/python3
""" 8-rectangle: class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        """Instantiates new Rectangle.
        Args:
            width (int): The width instance of the new Rectangle
            height (int): The height instance of the new Rectangle
        """

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):

        """
            returns area of Rectangle
        """
        return self.__width * self.__height

    def __str__(self):

        """
            string descriptor for Rectangle
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
