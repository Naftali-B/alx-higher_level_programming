#!/usr/bin/python3

""" Class Rectangle inherits from Base
    Private instance attributes,
    each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle.
            y (int): y-coordinate of the rectangle.
            id (int): Identifier of the rectangle.

        Returns:
            None
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width attribute.

        Returns:
            int: Width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width attribute.

        Args:
            value (int): Width to set.

        Returns:
            None
        """

        self.__check_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Get the height attribute.

        Returns:
            int: Height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height attribute.

        Args:
            value (int): Height to set.

        Returns:
            None
        """

        self.__check_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Get the x attribute.

        Returns:
            int: x-coordinate of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x attribute.

        Args:
            value (int): x-coordinate to set.

        Returns:
            None
        """

        self.__check_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Get the y attribute.

        Returns:
            int: y-coordinate of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y attribute.

        Args:
            value (int): y-coordinate to set.

        Returns:
            None
        """

        self.__check_non_negative_integer("y", value)
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """

        return self.width * self.height

    def display(self):
        """
        Print the rectangle using the '#' character.

        Returns:
            None
        """

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: Formatted string representation.
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update attributes of the Rectangle instance.

        Args:
            *args: Variable length argument list (no-keyword arguments).
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """

        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle instance.

        Returns:
            dict: Dictionary containing the attributes of the Rectangle.
        """

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __check_positive_integer(self, name, value):
        """
        Check if a value is a positive integer.

        Args:
            name (str): Name of the attribute being checked.
            value (int): Value to check.

        Returns:
            None

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def __check_non_negative_integer(self, name, value):
        """
        Check if a value is a non-negative integer.

        Args:
            name (str): Name of the attribute being checked.
            value (int): Value to check.

        Returns:
            None

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a non-negative integer.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
