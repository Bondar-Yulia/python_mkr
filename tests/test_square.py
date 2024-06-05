import unittest
from quadrilaterals.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        # Vertices for a square: (0,0), (2,0), (2,2), (0,2)
        self.shape = Square([(0, 0), (2, 0), (2, 2), (0, 2)])

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "Square")

    def test_is_square(self):
        self.assertTrue(self.shape.is_square)

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("Square"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_side_lengths(self):
        expected_lengths = [
            2.0,  # distance from (0,0) to (2,0)
            2.0,  # distance from (2,0) to (2,2)
            2.0,  # distance from (2,2) to (0,2)
            2.0   # distance from (0,2) to (0,0)
        ]
        side_lengths = self.shape.side_lengths
        for calculated, expected in zip(side_lengths, expected_lengths):
            self.assertAlmostEqual(calculated, expected, places=3)

    def test_perimeter(self):
        self.assertAlmostEqual(self.shape.perimeter, 8.0, places=3)

    def test_area(self):
        self.assertAlmostEqual(self.shape.area, 4.0, places=3)

if __name__ == "__main__":
    unittest.main()
