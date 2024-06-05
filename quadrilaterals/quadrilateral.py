from quadrilaterals.shape import AbstractShape
import math

class Quadrilateral(AbstractShape):
    def __init__(self, vertices):
        super().__init__()
        self._vertices = vertices
        self._side_lengths = self.calculate_side_lengths()
        self._perimeter = sum(self._side_lengths)
        self._area = self.calculate_area()
        self._diagonals = self.calculate_diagonals()
        self._angles = self.calculate_angles()

    @property
    def shape_type(self):
        return "Quadrilateral"

    @property
    def vertices(self):
        return self._vertices

    @property
    def side_lengths(self):
        return self._side_lengths

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def area(self):
        return self._area

    @property
    def diagonals(self):
        return self._diagonals

    @property
    def angles(self):
        return self._angles
    
    def get_vertices(self):
        return self._vertices

    def get_side_lengths(self):
        return self._side_lengths

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonals(self):
        return self._diagonals

    def get_angles(self):
        return self._angles


    @property
    def has_equal_sides(self):
        return len(set(self._side_lengths)) == 1

    @property
    def has_parallel_sides(self):
        def calculate_slope(p1, p2):
            try:
                return (p2[1] - p1[1]) / (p2[0] - p1[0])
            except ZeroDivisionError:
                return float('inf')
        
        slopes = [
            calculate_slope(self._vertices[i], self._vertices[(i + 1) % 4])
            for i in range(4)
        ]
        return slopes[0] == slopes[2] and slopes[1] == slopes[3]

    @property
    def has_opposite_angles_equal(self):
        return self._angles[0] == self._angles[2] and self._angles[1] == self._angles[3]

    @property
    def is_convex(self):
        return all(angle < 180 for angle in self._angles)

    def calculate_side_lengths(self):
        lengths = []
        for i in range(len(self._vertices)):
            p1 = self._vertices[i]
            p2 = self._vertices[(i + 1) % len(self._vertices)]
            length = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
            lengths.append(length)
        return lengths

    def calculate_area(self):
        x1, y1 = self._vertices[0]
        x2, y2 = self._vertices[1]
        x3, y3 = self._vertices[2]
        x4, y4 = self._vertices[3]
        return 0.5 * abs(x1*y2 + x2*y3 + x3*y4 + x4*y1 - (y1*x2 + y2*x3 + y3*x4 + y4*x1))

    def calculate_diagonals(self):
        d1 = math.sqrt((self._vertices[2][0] - self._vertices[0][0]) ** 2 + (self._vertices[2][1] - self._vertices[0][1]) ** 2)
        d2 = math.sqrt((self._vertices[3][0] - self._vertices[1][0]) ** 2 + (self._vertices[3][1] - self._vertices[1][1]) ** 2)
        return d1, d2

    def calculate_angles(self):
        def angle(a, b, c):
            ab = (b[0] - a[0], b[1] - a[1])
            bc = (c[0] - b[0], c[1] - b[1])
            dot_product = ab[0] * bc[0] + ab[1] * bc[1]
            mag_ab = math.sqrt(ab[0]**2 + ab[1]**2)
            mag_bc = math.sqrt(bc[0]**2 + bc[1]**2)
            cos_theta = dot_product / (mag_ab * mag_bc)
            # Handle potential floating-point precision errors
            cos_theta = min(1, max(-1, cos_theta))
            return math.degrees(math.acos(cos_theta))
        
        angles = []
        for i in range(len(self._vertices)):
            a = self._vertices[i - 1]
            b = self._vertices[i]
            c = self._vertices[(i + 1) % len(self._vertices)]
            angles.append(angle(a, b, c))
        return angles

    def is_instance_of(self, shape_type):
        return self.shape_type == shape_type

    def compare_area(self, other):
        return self.area - other.area

    def compare_perimeter(self, other):
        return self.perimeter - other.perimeter

    def compare_area_and_perimeter(self, other):
        return (self.area, self.perimeter) - (other.area, other.perimeter)

    def intersects_with(self, other):
        def do_intersect(p1, q1, p2, q2):
            def orientation(p, q, r):
                val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
                if val == 0:
                    return 0
                elif val > 0:
                    return 1
                else:
                    return 2

            def on_segment(p, q, r):
                if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
                    return True
                return False

            o1 = orientation(p1, q1, p2)
            o2 = orientation(p1, q1, q2)
            o3 = orientation(p2, q2, p1)
            o4 = orientation(p2, q2, q1)

            if o1 != o2 and o3 != o4:
                return True

            if o1 == 0 and on_segment(p1, p2, q1):
                return True

            if o2 == 0 and on_segment(p1, q2, q1):
                return True

            if o3 == 0 and on_segment(p2, p1, q2):
                return True

            if o4 == 0 and on_segment(p2, q1, q2):
                return True

            return False

        for i in range(len(self._vertices)):
            for j in range(len(other.vertices)):
                if do_intersect(self._vertices[i], self._vertices[(i + 1) % len(self._vertices)],
                                other.vertices[j], other.vertices[(j + 1) % len(other.vertices)]):
                    return True

        return False
