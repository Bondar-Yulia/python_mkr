from quadrilaterals.quadrilateral import Quadrilateral

class Parallelogram(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        if not self.is_parallelogram:
            raise ValueError("A parallelogram must have opposite sides parallel.")

    @property
    def shape_type(self):
        return "Parallelogram"
    
    @property
    def is_parallelogram(self):
        return self.has_parallel_sides
    
    def is_instance_of(self, shape_type):
        return shape_type == "Parallelogram" or super().is_instance_of(shape_type)


