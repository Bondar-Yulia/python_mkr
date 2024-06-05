from quadrilaterals.trapezoid import Trapezoid

class IsoscelesTrapezoid(Trapezoid):
    def __init__(self, vertices):
        super().__init__(vertices)
        if not self.has_equal_legs:
            raise ValueError("An isosceles trapezoid must have legs of equal length.")

    @property
    def shape_type(self):
        return "Isosceles Trapezoid"
    
    @property
    def has_equal_legs(self):
        sides = self._side_lengths

        def is_parallel(line1, line2):
            dx1, dy1 = line1[1][0] - line1[0][0], line1[1][1] - line1[0][1]
            dx2, dy2 = line2[1][0] - line2[0][0], line2[1][1] - line2[0][1]
            return dx1 * dy2 == dy1 * dx2
        
        vertices_pairs = [
            (self._vertices[0], self._vertices[1]),
            (self._vertices[1], self._vertices[2]),
            (self._vertices[2], self._vertices[3]),
            (self._vertices[3], self._vertices[0])
        ]
        
        parallel_pairs = [
            (0, 2) if is_parallel(vertices_pairs[0], vertices_pairs[2]) else None,
            (1, 3) if is_parallel(vertices_pairs[1], vertices_pairs[3]) else None
        ]
        
        parallel_pairs = [pair for pair in parallel_pairs if pair is not None]
        
        if not parallel_pairs:
            return False
        
        legs_indices = [i for i in range(4) if i not in parallel_pairs[0]]
        
        return abs(sides[legs_indices[0]] - sides[legs_indices[1]]) < 1e-6
    
    def is_instance_of(self, shape_type):
        return shape_type == "Isosceles Trapezoid" or super().is_instance_of(shape_type)