from quadrilaterals.trapezoid import Trapezoid

class RightTrapezoid(Trapezoid):
    def __init__(self, vertices):
        super().__init__(vertices)
        if not self.has_right_angles:
            raise ValueError("A right trapezoid must have two right angles.")
    
    @property
    def shape_type(self):
        return "Right Trapezoid"
    
    @property
    def has_right_angles(self):
        right_angle_tolerance = 1e-6 
        right_angles = [angle for angle in self._angles if abs(angle - 90) < right_angle_tolerance]
        return len(right_angles) == 2

    def is_instance_of(self, shape_type):
        return shape_type == "Right Trapezoid" or super().is_instance_of(shape_type)

