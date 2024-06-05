import unittest
from quadrilaterals.parallelogram import Parallelogram

class TestParallelogram(unittest.TestCase):
    def setUp(self):
        # Vertices for a parallelogram: (0,0), (3,0), (4,2), (1,2)
        self.shape = Parallelogram([(0, 0), (3, 0), (4, 2), (1, 2)])

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "Parallelogram")

    def test_is_parallelogram(self):
        self.assertTrue(self.shape.is_parallelogram)

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("Parallelogram"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_side_lengths(self):
        expected_lengths = [
            3.0,  # distance from (0,0) to (3,0)
            2.236,  # distance from (3,0) to (4,2)
            3.0,  # distance from (4,2) to (1,2)
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
