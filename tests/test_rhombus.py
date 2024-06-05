import unittest
from quadrilaterals.rhombus import Rhombus

class TestRhombus(unittest.TestCase):
    def setUp(self):
        # Vertices for a rhombus: (0,0), (2,1), (0,2), (-2,1)
        self.shape = Rhombus([(0, 0), (2, 1), (0, 2), (-2, 1)])

    def test_shape_type(self):
        self.assertEqual(self.shape.shape_type, "Rhombus")

    def test_is_rhombus(self):
        self.assertTrue(self.shape.is_rhombus)

    def test_is_instance_of(self):
        self.assertTrue(self.shape.is_instance_of("Rhombus"))
        self.assertFalse(self.shape.is_instance_of("OtherShape"))

    def test_side_lengths(self):
        expected_lengths = [
            2.236,  # distance from (0,0) to (2,1)
            2.236,  # distance from (2,1) to (0,2)
            2.236,  # distance from (0,2) to (-2,1)
            2.236   # distance from (-2,1) to (0,0)
        ]
        side_lengths = self.shape.side_lengths
        for calculated, expected in zip(side_lengths, expected_lengths):
            self.assertAlmostEqual(calculated, expected, places=3)

    def test_perimeter(self):
        self.assertAlmostEqual(self.shape.perimeter, 8.944, places=3)

    def test_area(self):
        self.assertAlmostEqual(self.shape.area, 4.0, places=3)

if __name__ == "__main__":
    unittest.main()
