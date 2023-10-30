#!/usr/bin/python3
"""
6-rectangle: Defines the Rectangle class.
"""

class Rectangle:
    """
    Rectangle class: Defines a rectangle object.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    
    number_of_instances = 0  # Class attribute to keep track of the number of instances

    def __init__(self, width=0, height=0):
        """
        Initializes the attributes for instances and increments the instance count.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the private attribute 'width'.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the private attribute 'width'.

        Args:
            value (int): The new width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the private attribute 'height'.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the private attribute 'height'.

        Args:
            value (int): The new height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters.
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width

        return rectangle

    def __repr__(self):
        """
        Returns a string representation of the object to recreate it using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted and decrements the instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
