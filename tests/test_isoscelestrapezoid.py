import unittest
from quadrilaterals.isoscelestrapezoid import IsoscelesTrapezoid

class TestIsoscelesTrapezoid(unittest.TestCase):
    def setUp(self):
        # Vertices for an isosceles trapezoid: (0,0), (4,0), (3,2), (1,2)
        self.shape = IsoscelesTrapezoid([(0, 0), (4, 0), (3, 2), (1, 2)])

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "Isosceles Trapezoid")

    def test_has_equal_legs(self):
        self.assertTrue(self.shape.has_equal_legs)

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("Isosceles Trapezoid"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_side_lengths(self):
        expected_lengths = [
            4.0,  # distance from (0,0) to (4,0)
            2.236,  # distance from (4,0) to (3,2)
            2.0,  # distance from (3,2) to (1,2)
            2.236   # distance from (1,2) to (0,0)
        ]
        side_lengths = self.shape.side_lengths
        for calculated, expected in zip(side_lengths, expected_lengths):
            self.assertAlmostEqual(calculated, expected, places=3)

    def test_perimeter(self):
        self.assertAlmostEqual(self.shape.perimeter, 10.472, places=3)

    def test_area(self):
        self.assertAlmostEqual(self.shape.area, 6.0, places=3)

if __name__ == "__main__":
    unittest.main()
