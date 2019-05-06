class Student:

    def __init__(self, name, cpr):
        self.__name = name
        self.__cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return f'Im Anna, im the daughter of {self.name} :)'

    def __len__(self):
        return 180

    def __str__(self):
        return self.name + ' '

    def __repr__(self):
        return '{name : self.name}'
    


