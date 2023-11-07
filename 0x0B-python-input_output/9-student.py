#!/usr/bin/python3
""" 9-student: class Student """


class Student:
    """
        Attributes:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
    """
    def __init__(self, first_name, last_name, age):
        """
            Instantiation with first_name, last_name and age
        """i

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves dict representation of instances
        """
        return self.__dict__
