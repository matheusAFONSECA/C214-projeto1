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


if __name__ == "__main__":
    unittest.main()
