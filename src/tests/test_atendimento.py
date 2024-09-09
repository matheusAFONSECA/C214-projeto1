import unittest
from src.modules.modules import assign_building


class TestAtendimento(unittest.TestCase):
    """
    The assign_building function assigns a
    building based on the room numbers.
    These tests ensure correct assignment
    for success and failure scenarios.
    """

    def test_assign_building_sala_1_a_5(self):
        """
        Success case: Test to assign 1 to 5 to building 1.
        """
        self.assertEqual(assign_building(3), "1")
        self.assertEqual(assign_building(1), "1")
        self.assertEqual(assign_building(5), "1")

    def test_assign_building_sala_6_a_10(self):
        """
        Success case: Test to assign 6 to 10 to building 2.
        """
        self.assertEqual(assign_building(6), "2")
        self.assertEqual(assign_building(9), "2")
        self.assertEqual(assign_building(10), "2")

    def test_assign_building_acima_10(self):
        """
        Success case: Test to assign above 10 to 'Other'.
        """
        self.assertEqual(assign_building(11), "Outro")
        self.assertEqual(assign_building(20), "Outro")

    def test_assign_building_abaixo_1(self):
        """
        Success case: Test for below 1 being assigned to 'Other'.
        """
        self.assertEqual(assign_building(0), "Outro")
        self.assertEqual(assign_building(-5), "Outro")

    def test_assign_building_sala_invalida(self):
        """
        Failure case: Test for invalid (non-integer) entry.
        """
        with self.assertRaises(ValueError):
            assign_building("invalid")


if __name__ == "__main__":
    unittest.main()
