import unittest
from quadrilaterals.righttrapezoid import RightTrapezoid

class TestRightTrapezoid(unittest.TestCase):
    def setUp(self):
        # Example vertices that form a right trapezoid
        # Vertices: (0,0), (3,0), (2,1), (0,1)
        self.shape = RightTrapezoid([(0, 0), (3, 0), (2, 1), (0, 1)])

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "Right Trapezoid")

    def test_has_right_angles(self):
        self.assertTrue(self.shape.has_right_angles)

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("Right Trapezoid"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_side_lengths(self):
        expected_lengths = [
            3.0,  # distance from (0,0) to (3,0)
            1.414,  # distance from (3,0) to (2,1)
            2.0,  # distance from (2,1) to (0,1)
            1.0   # distance from (0,1) to (0,0)
        ]
        side_lengths = self.shape.side_lengths
        for calculated, expected in zip(side_lengths, expected_lengths):
            self.assertAlmostEqual(calculated, expected, places=3)

    def test_perimeter(self):
        self.assertAlmostEqual(self.shape.perimeter, 7.414, places=3)

    def test_area(self):
        self.assertAlmostEqual(self.shape.area, 2.5, places=3)

if __name__ == "__main__":
    unittest.main()
