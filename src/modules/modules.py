import json

# Path to your JSON file
json_file_path = "data/dados.json"


def load_json_data(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: Data loaded from the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def assign_building(room):
    """
    Assign a building based on the provided room number.

    Args:
        room (int): Room number.

    Returns:
        str: The corresponding building:
             - "1" for rooms 1 to 5,
             - "2" for rooms 6 to 10,
             - "Other" for rooms greater than 10 or less than 1.

    Raises:
        ValueError: If the room is not an integer.
    """
    if isinstance(room, bool): 
        raise ValueError(f"Invalid room: {room}. Cannot be a boolean.")
    if not isinstance(room, int):
        raise ValueError(f"Invalid room: {room}. Must be an integer.")

    if 1 <= room <= 5:
        return "1"
    elif 6 <= room <= 10:
        return "2"
    else:
        return "Outro"
    

def validate_professor_name(name):
    """
    Validate if the given professor name is valid and return it.

    Args:
        name (str): Name of the professor.

    Returns:
        str: The validated professor name.

    Raises:
        ValueError: If the name is not a valid string.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Invalid name: The name must be a non-empty string.")
    
    # Additional logic could be added here for further validation if needed
    return name



def process_professor_data(professor_data):
    """
    Process professor data, assign the building based on the room, and print the information.

    Args:
        professor_data (dict): A dictionary containing professor information.

    Raises:
        ValueError: If data is empty or period is not a string.
        TypeError: If 'predio' is not a list.
    """
    if not professor_data:
        raise ValueError("Professor data cannot be empty.")

    for professor, data in professor_data.items():
        if not isinstance(data["periodo"], str):
            raise ValueError(f"Invalid period: {data['periodo']}. Must be a string.")

        if not isinstance(data["predio"], list):
            raise TypeError(f"Invalid 'predio' type: {data['predio']}. Must be a list.")

        room = int(data["sala"])
        building = assign_building(room)

        print(f"Professor: {data['nomeDoProfessor']}")
        print(f"Office Hours: {data['horarioDeAtendimento']}")
        print(f"Period: {data['periodo']}")
        print(f"Room: {room}")
        print(f"Assigned Building: {building}")
        print(f"Available Buildings: {', '.join(data['predio'])}")
        print("-" * 40)



if __name__ == "__main__":
    # Load data from the JSON file and process professor information.
    professor_data = load_json_data(json_file_path)
    process_professor_data(professor_data)
