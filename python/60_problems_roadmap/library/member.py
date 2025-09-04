from uuid import uuid4

from .descriptors import PositiveNumber, UpperCaseDescriptor
from .library import Library


class Member:

    name = UpperCaseDescriptor()
    age = PositiveNumber()

    def __init__(self, name, age, library: Library):
        self.__id = None
        self.name = name
        self.age = age
        self.library = self.__subscribe(library)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_value):
        self.__id = id_value

    def __subscribe(self, library):
        if not isinstance(library, Library):
            raise ValueError("Library must be an instance of Library class")
        self.id = uuid4()
        library.add_member(self)
        return library

    def __repr__(self):
        return f"<Member id={self.id!r}, name={self.name!r}, age={self.age}>"
