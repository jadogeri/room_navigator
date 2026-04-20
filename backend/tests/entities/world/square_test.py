import unittest
from typing import Optional

from src.entities.world.square import Square

class TestSquare(unittest.TestCase):
    
    def setUp(self):
        """Setup: Create fresh instances for every test."""
        self.center = Square() # pyright: ignore[reportUndefinedVariable]
        self.north_sq = Square()
        self.south_sq = Square()
        self.east_sq = Square()
        self.west_sq = Square()

    def tearDown(self):
        """Teardown: Explicitly clear references."""
        self.center = None
        self.north_sq = None
        self.south_sq = None
        self.east_sq = None
        self.west_sq = None

    # --- Group 1: Initialization Tests ---
    def test_01_init_north(self):
        sq = Square(north=self.north_sq)
        self.assertIs(sq.north, self.north_sq)

    def test_02_init_south(self):
        sq = Square(south=self.south_sq)
        self.assertIs(sq.south, self.south_sq)

    def test_03_init_east(self):
        sq = Square(east=self.east_sq)
        self.assertIs(sq.east, self.east_sq)

    def test_04_init_west(self):
        sq = Square(west=self.west_sq)
        self.assertIs(sq.west, self.west_sq)

    # --- Group 2: Auto-Linking Tests ---
    def test_05_auto_link_north_sets_south(self):
        self.center.north = self.north_sq
        self.assertIs(self.north_sq.south, self.center)

    def test_06_auto_link_south_sets_north(self):
        self.center.south = self.south_sq
        self.assertIs(self.south_sq.north, self.center)

    def test_07_auto_link_east_sets_west(self):
        self.center.east = self.east_sq
        self.assertIs(self.east_sq.west, self.center)

    def test_08_auto_link_west_sets_east(self):
        self.center.west = self.west_sq
        self.assertIs(self.west_sq.east, self.center)

    # --- Group 3: Validation Tests ---
    def test_09_invalid_type_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.center.north = "not a square"

    def test_10_none_assignment_is_valid(self):
        self.center.north = self.north_sq
        self.center.north = None
        self.assertIsNone(self.center.north)

    # --- Group 4: Complex Grid/Structure Tests ---
    def test_11_reassignment_updates_reciprocal(self):
        new_north = Square()
        self.center.north = self.north_sq
        self.center.north = new_north
        self.assertIs(new_north.south, self.center)

    def test_12_circular_link_diamond(self):
        # A.north -> B, B.east -> C, C.south -> D, D.west -> A
        # Tests multiple connections simultaneously
        sq_a, sq_b, sq_c, sq_d = Square(), Square(), Square(), Square()
        sq_a.north = sq_b
        sq_b.east = sq_c
        sq_c.south = sq_d
        sq_d.west = sq_a
        self.assertIs(sq_b.south, sq_a)
        self.assertIs(sq_c.west, sq_b)

    # --- Group 5: Method & Identity Tests ---
    def test_13_repr_indicates_neighbor_presence(self):
        self.center.north = self.north_sq
        self.assertIn("N:Square", repr(self.center))
        self.assertIn("S:None", repr(self.center))

    def test_14_to_dict_structure(self):
        d = self.center.to_dict()
        expected_keys = {"north", "south", "east", "west", "id", "occupant"}
        self.assertEqual(set(d.keys()), expected_keys)

    def test_15_equality_checks_identity(self):
        # Even if values look same, identity must match
        other_center = Square()
        self.assertNotEqual(self.center, other_center)

    def test_16_hash_is_consistent(self):
        initial_hash = hash(self.center)
        self.center.north = self.north_sq
        self.assertEqual(initial_hash, hash(self.center))

if __name__ == '__main__':
    unittest.main()
