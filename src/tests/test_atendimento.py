import unittest
from src.modules.modules import assign_building


class TestAtendimento(unittest.TestCase):
    """
    The assign_building function assigns a
    building based on the room numbers.
    These tests ensure correct assignment
    for success and failure scenarios.
    """

    """------------------- Success cases -------------------"""

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

    """------------------- Failure cases -------------------"""

    def test_assign_building_sala_invalida(self):
        """
        Failure case: Test for invalid (non-integer) entry.
        """
        with self.assertRaises(ValueError):
            assign_building("invalid")

    def test_assign_building_com_string_numero(self):
        """
        Failure case: Test for string input with a number.
        """
        with self.assertRaises(ValueError):
            assign_building("5")

    def test_assign_building_com_lista(self):
        """
        Failure case: Test for input as a list.
        """
        with self.assertRaises(ValueError):
            assign_building([1, 2, 3])

    def test_assign_building_com_dicionario(self):
        """
        Failure case: Test for input as a dictionary.
        """
        with self.assertRaises(ValueError):
            assign_building({"sala": 3})

    def test_assign_building_com_none(self):
        """
        Failure case: Test for input as None.
        """
        with self.assertRaises(ValueError):
            assign_building(None)

    def test_assign_building_com_numero_flutuante(self):
        """
        Failure case: Test for input as a float.
        """
        with self.assertRaises(ValueError):
            assign_building(5.5)
            
    def test_assign_building_boolean(self):
        """
        Failure case: Test for boolean input (True or False).
        """
        with self.assertRaises(ValueError):
            assign_building(True)
        with self.assertRaises(ValueError):
            assign_building(False)

if __name__ == "__main__":
    unittest.main()
