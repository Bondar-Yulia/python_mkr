import unittest
from quadrilaterals.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        # Vertices for a rectangle: (0,0), (3,0), (3,2), (0,2)
        self.shape = Rectangle([(0, 0), (3, 0), (3, 2), (0, 2)])

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "Rectangle")

    def test_is_rectangle(self):
        self.assertTrue(self.shape.is_rectangle)

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("Rectangle"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_side_lengths(self):
        expected_lengths = [
            3.0,  # distance from (0,0) to (3,0)
            2.0,  # distance from (3,0) to (3,2)
            3.0,  # distance from (3,2) to (0,2)
            2.0   # distance from (0,2) to (0,0)
        ]
        side_lengths = self.shape.side_lengths
        for calculated, expected in zip(side_lengths, expected_lengths):
            self.assertAlmostEqual(calculated, expected, places=3)

    def test_perimeter(self):
        self.assertAlmostEqual(self.shape.perimeter, 10.0, places=3)

    def test_area(self):
        self.assertAlmostEqual(self.shape.area, 6.0, places=3)

if __name__ == "__main__":
    unittest.main()
