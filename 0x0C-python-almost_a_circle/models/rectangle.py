#!/usr/bin/python3

"""Class Rectangle inherits from Base
    Private instance attributes,
    each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
"""


from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super()__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("Width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("Height must be an integer")
        elif value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("X must be an integer")
        elif value < 0:
            raise ValueError("X must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError("Y must be an integer")
        elif value < 0:
            raise ValueError("Y must be >= 0")
        self.__y = value


