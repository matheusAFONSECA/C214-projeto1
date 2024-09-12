import unittest
from unittest.mock import patch
from src.modules.modules import process_professor_data


class TestProfessorData(unittest.TestCase):
    """
    Tests for the professor_data function
    with mock of teacher data.
    """

    @patch("src.modules.modules.json")
    def test_process_professor_data(self, mock_json):
        """
        Test for teacher_data using mocked teacher data.
        """
        mock_professor_data = {
            "prof1": {
                "nomeDoProfessor": "Marcelo Cisneyros",
                "horarioDeAtendimento": "19:30",
                "periodo": "Noturno",
                "sala": "3",
                "predio": ["1", "2", "3", "4", "6"],
            },
            "prof2": {
                "nomeDoProfessor": "Chris Lima",
                "horarioDeAtendimento": "15:30",
                "periodo": "Integral",
                "sala": "1",
                "predio": ["1", "2", "3", "4", "6"],
            },
            "prof3": {
                "nomeDoProfessor": "RenZo",
                "horarioDeAtendimento": "17:30",
                "periodo": "Integral",
                "sala": "7",
                "predio": ["1", "2", "3", "4", "6"],
            },
            "prof4": {
                "nomeDoProfessor": "ThiThi Miguelito",
                "horarioDeAtendimento": "19:30",
                "periodo": "Noturno",
                "sala": "14",
                "predio": ["1", "2", "3", "4", "6"],
            },
            "prof5": {
                "nomeDoProfessor": "Evandro César Vilas Boas",
                "horarioDeAtendimento": "08:00",
                "periodo": "Integral",
                "sala": "2",
                "predio": ["1", "2", "3", "4", "6"],
            },
        }

        mock_json.return_value = mock_professor_data
        process_professor_data(mock_json.return_value)
