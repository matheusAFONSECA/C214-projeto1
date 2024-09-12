import unittest
from src.modules.modules import process_professor_data


class TestProfessorData(unittest.TestCase):
    """
    Tests for the process_professor_data function.
    """

    """------------------- Failure cases -------------------"""

    def test_process_professor_data_missing_name(self):
        """
        Failure case: Test when 'nomeDoProfessor' is missing.
        """
        incomplete_data = {
            "prof1": {
                "horarioDeAtendimento": "19:30",
                "periodo": "Noturno",
                "sala": "3",
                "predio": ["1", "2", "3", "4", "6"],
            }
        }
        with self.assertRaises(KeyError):
            process_professor_data(incomplete_data)

    def test_process_professor_data_invalid_room(self):
        """
        Failure case: Test when 'sala' is invalid (string instead of int).
        """
        invalid_data = {
            "prof1": {
                "nomeDoProfessor": "Marcelo Cisneyros",
                "horarioDeAtendimento": "19:30",
                "periodo": "Noturno",
                "sala": "three",
                "predio": ["1", "2", "3", "4", "6"],
            }
        }
        with self.assertRaises(ValueError):
            process_professor_data(invalid_data)

    def test_process_professor_data_empty_data(self):
        """
        Failure case: Test when data is empty.
        """
        empty_data = {}
        with self.assertRaises(ValueError):
            process_professor_data(empty_data)

    def test_process_professor_data_invalid_predio_type(self):
        """
        Failure case: Test when 'predio' is not a list.
        """
        invalid_data = {
            "prof1": {
                "nomeDoProfessor": "Marcelo Cisneyros",
                "horarioDeAtendimento": "19:30",
                "periodo": "Noturno",
                "sala": "3",
                "predio": "1234",
            }
        }
        with self.assertRaises(TypeError):
            process_professor_data(invalid_data)

    def test_process_professor_data_invalid_period(self):
        """
        Failure case: Test when 'periodo' is invalid (not string).
        """
        invalid_data = {
            "prof1": {
                "nomeDoProfessor": "Marcelo Cisneyros",
                "horarioDeAtendimento": "19:30",
                "periodo": 123,
                "sala": "3",
                "predio": ["1", "2", "3", "4", "6"],
            }
        }
        with self.assertRaises(ValueError):
            process_professor_data(invalid_data)


if __name__ == "__main__":
    unittest.main()
