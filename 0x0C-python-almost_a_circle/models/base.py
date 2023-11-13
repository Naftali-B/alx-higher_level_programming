#!/usr/bin/python3

    """
    Class Base:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)::
        if id is not None, assign the public instance attribute id
        with this argument value - you can assume id is an integer
        otherwise, increment __nb_objects
        and assign the new value to the public instance attribute id
        
        This class will be the “base” of all other classes in this project.
    """


import json

class Base:
    """Base class for managing id attribute in all classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance with an id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a file in JSON format.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes from a dictionary.

        Args:
            dictionary (dict): Dictionary with instance attributes.

        Returns:
            Base: Instance with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Creating a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Creating a dummy Square instance
        else:
            dummy_instance = None

        dummy_instance.update(**dictionary)  # Updating dummy instance with real values
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a file in JSON format.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                return [cls.create(**dic) for dic in dictionaries]
        except FileNotFoundError:
            return []


