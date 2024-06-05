from quadrilaterals.parallelogram import Parallelogram

class Rhombus(Parallelogram):
    def __init__(self, vertices):
        super().__init__(vertices)
        if not self.is_rhombus:
            raise ValueError("A rhombus must have all sides equal.")

    @property
    def shape_type(self):
        return "Rhombus"
    
    @property
    def is_rhombus(self):
        return self.has_equal_sides
    
    def is_instance_of(self, shape_type):
        return shape_type == "Rhombus" or super().is_instance_of(shape_type)