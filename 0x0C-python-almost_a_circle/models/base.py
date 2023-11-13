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

Class Base(self):
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
