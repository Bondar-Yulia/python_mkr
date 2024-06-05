# AbstractShape.py
from abc import ABC, abstractmethod
import uuid

class AbstractShape(ABC):
    def __init__(self):
        self._id = f"{self.shape_type}_{uuid.uuid4()}"
    
    @property
    @abstractmethod
    def shape_type(self):
        pass

    @property
    def id(self):
        return self._id

    @property
    @abstractmethod
    def vertices(self):
        pass

    @property
    @abstractmethod
    def side_lengths(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def diagonals(self):
        pass

    @property
    @abstractmethod
    def angles(self):
        pass

    @abstractmethod
    def get_vertices(self):
        pass

    @abstractmethod
    def get_side_lengths(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_diagonals(self):
        pass

    @abstractmethod
    def get_angles(self):
        pass

    @classmethod
    def get_subtypes(cls):
        def recursive_subtypes(cls):
            subclasses = cls.__subclasses__()
            for subclass in subclasses:
                yield subclass
                yield from recursive_subtypes(subclass)

        return list(recursive_subtypes(cls))

    @classmethod
    def get_supertypes(cls):
        return list(cls.__mro__)

    @abstractmethod
    def is_instance_of(self, shape_type):
        pass

    @abstractmethod
    def compare_area(self, other):
        pass

    @abstractmethod
    def compare_perimeter(self, other):
        pass

    @abstractmethod
    def compare_area_and_perimeter(self, other):
        pass

    @abstractmethod
    def intersects_with(self, other):
        pass
