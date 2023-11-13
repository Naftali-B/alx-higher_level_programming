#!/usr/bin/python3
    """
    Class Square inherits from Rectangle
    Class constructor:
    def __init__(self, size, x=0, y=0, id=None)::
    Call the super class with id, x, y, width and height
    - this super call will use the logic
    of the __init__ of the Rectangle class.
    """


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Side length of the square.
            x (int): x-coordinate of the square.
            y (int): y-coordinate of the square.
            id (int): Identifier of the square.

        Returns:
            None
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size attribute.

        Returns:
            int: Size of the square.
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size attribute.

        Args:
            value (int): Size to set.

        Returns:
            None
        """

        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: Formatted string representation.
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square instance.

        Args:
            *args: Variable length argument list (no-keyword arguments).
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """

        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Square instance.

        Returns:
            dict: Dictionary containing the attributes of the Square.
        """

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
