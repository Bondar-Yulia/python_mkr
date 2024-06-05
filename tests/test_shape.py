import unittest
from quadrilaterals.shape import AbstractShape

class ConcreteShape(AbstractShape):
    @property
    def shape_type(self):
        return "TestShape"

    @property
    def vertices(self):
        return [(0, 0), (1, 0), (1, 1), (0, 1)]

    @property
    def side_lengths(self):
        return [1, 1, 1, 1]

    @property
    def perimeter(self):
        return 4

    @property
    def area(self):
        return 1

    @property
    def diagonals(self):
        return [1.414, 1.414]

    @property
    def angles(self):
        return [90, 90, 90, 90]

    def get_vertices(self):
        return self.vertices

    def get_side_lengths(self):
        return self.side_lengths

    def get_perimeter(self):
        return self.perimeter

    def get_area(self):
        return self.area

    def get_diagonals(self):
        return self.diagonals

    def get_angles(self):
        return self.angles

    def is_instance_of(self, shape_type):
        return shape_type == "TestShape"

    def compare_area(self, other):
        return self.area - other.area

    def compare_perimeter(self, other):
        return self.perimeter - other.perimeter

    def compare_area_and_perimeter(self, other):
        return (self.area - other.area, self.perimeter - other.perimeter)

    def intersects_with(self, other):
        return False

class TestAbstractShape(unittest.TestCase):
    def setUp(self):
        self.shape = ConcreteShape()

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "TestShape")

    def test_id(self):
        self.assertTrue(self.shape.id.startswith("TestShape_"))

    def test_vertices(self):
        self.assertEqual(self.shape.vertices, [(0, 0), (1, 0), (1, 1), (0, 1)])

    def test_side_lengths(self):
        self.assertEqual(self.shape.side_lengths, [1, 1, 1, 1])

    def test_perimeter(self):
        self.assertEqual(self.shape.perimeter, 4)

    def test_area(self):
        self.assertEqual(self.shape.area, 1)

    def test_diagonals(self):
        self.assertEqual(self.shape.diagonals, [1.414, 1.414])

    def test_angles(self):
        self.assertEqual(self.shape.angles, [90, 90, 90, 90])

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("TestShape"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_compare_area(self):
        other_shape = ConcreteShape()
        self.assertEqual(self.shape.compare_area(other_shape), 0)

    def test_compare_perimeter(self):
        other_shape = ConcreteShape()
        self.assertEqual(self.shape.compare_perimeter(other_shape), 0)

    def test_compare_area_and_perimeter(self):
        other_shape = ConcreteShape()
        self.assertEqual(self.shape.compare_area_and_perimeter(other_shape), (0, 0))

    def test_intersects_with(self):
        other_shape = ConcreteShape()
        self.assertFalse(self.shape.intersects_with(other_shape))

if __name__ == "__main__":
    unittest.main()
