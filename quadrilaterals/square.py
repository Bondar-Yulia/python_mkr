from quadrilaterals.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        if not self.is_square:
            raise ValueError("A square must have all sides equal.")

    @property
    def shape_type(self):
        return "Square"
    
    @property
    def is_square(self):
        return self.has_equal_sides
    
    def is_instance_of(self, shape_type):
        return shape_type == "Square" or super().is_instance_of(shape_type)
