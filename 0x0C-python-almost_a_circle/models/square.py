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
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
