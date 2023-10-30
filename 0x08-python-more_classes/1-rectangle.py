#!/usr/bin/python3
""" Rectangle class """

class Rectangle:
    """
    width (int)
    height (int)
    The __init__: Initializes width and height for all instances
    """

    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0

        """
        Property setters to validate and set the initial values
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter function for width
            Return:
                width of rectangle
        """
        return self._width

    @width.setter
    def width(self, value):
        """ setter function for width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ getter function for height
            Return:
                height of rectangle
        """

        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
