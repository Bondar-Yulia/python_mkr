from quadrilaterals.quadrilateral import Quadrilateral

class Trapezoid(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        if not self.has_parallel_sides:
            raise ValueError("A trapezoid must have at least one pair of parallel sides.")

    @property
    def shape_type(self):
        return "Trapezoid"
    
    @property
    def has_parallel_sides(self):
        def are_parallel(v1, v2, v3, v4):
            return (v2[1] - v1[1]) * (v4[0] - v3[0]) == (v4[1] - v3[1]) * (v2[0] - v1[0])

        return (are_parallel(self._vertices[0], self._vertices[1], self._vertices[2], self._vertices[3]) or
                are_parallel(self._vertices[1], self._vertices[2], self._vertices[3], self._vertices[0]))

    def is_instance_of(self, shape_type):
        return shape_type == "Trapezoid" or super().is_instance_of(shape_type)

