import unittest
from quadrilaterals.quadrilateral import Quadrilateral

class TestQuadrilateral(unittest.TestCase):
    def setUp(self):
        # Vertices for a generic quadrilateral: (0,0), (2,0), (3,2), (1,3)
        self.shape = Quadrilateral([(0, 0), (2, 0), (3, 2), (1, 3)])

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "Quadrilateral")

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("Quadrilateral"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_side_lengths(self):
        expected_lengths = [
            2.0,  # distance from (0,0) to (2,0)
            2.236,  # distance from (2,0) to (3,2)
            2.236,  # distance from (3,2) to (1,3)
            3.162   # distance from (1,3) to (0,0)
        ]
        side_lengths = self.shape.side_lengths
        for calculated, expected in zip(side_lengths, expected_lengths):
            self.assertAlmostEqual(calculated, expected, places=3)

    def test_perimeter(self):
        self.assertAlmostEqual(self.shape.perimeter, 9.634, places=3)

    def test_area(self):
        # Updated expected area value based on actual calculation
        self.assertAlmostEqual(self.shape.area, 5.5, places=3)

if __name__ == "__main__":
    unittest.main()
