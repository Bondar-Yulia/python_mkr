from quadrilaterals.parallelogram import Parallelogram

class Rectangle(Parallelogram):
    def __init__(self, vertices):
        super().__init__(vertices)
        if not self.is_rectangle:
            raise ValueError("A rectangle must have all angles equal to 90 degrees.")

    @property
    def shape_type(self):
        return "Rectangle"
    
    @property
    def is_rectangle(self):
        return all(angle == 90 for angle in self._angles)
    
    def is_instance_of(self, shape_type):
        return shape_type == "Rectangle" or super().is_instance_of(shape_type)