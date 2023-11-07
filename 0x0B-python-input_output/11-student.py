#!/usr/bin/python3
""" defines a student by: (based on 10-student.py) """


class Student:
    """
        class Student
        Attributes:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
    """

    def __init__(self, first_name, last_name, age):
        """
            initializes values for all instances
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves dict representation

        """
        if isinstance(attrs, list) and all(
                isinstance(s, str) for s in attrs):
            return {el: getattr(self, el) for el in attrs if hasattr(self, el)}
        return self.__dict__

    def reload_from_json(self, json):
        """
            replaces attributes of Student
        """

        if json:
            for key, value in json.items():
                setattr(self, key, value)
