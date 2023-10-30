#!/usr/bin/python3
""" Module defining the Rectangle class. """

class Rectangle:
    """
    Rectangle class: defines a rectangle.
    
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    
    Methods:
        __init__: Initializes width and height for all instances.
    """

    def __init__(self, width=0, height=0):
        """ Initializes attributes for instances.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width
        else:
            raise TypeError('width must be an integer')

        if isinstance(height, int):
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        """ Getter method for the width attribute.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for the width attribute.

        Args:
            value (int): The new width value.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Getter method for the height attribute.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for the height attribute.

        Args:
            value (int): The new height value.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

