import os

def read_boolean_from_file(filename: str):
    if not os.path.isfile(filename):
        _write_boolean_to_file(filename, False)
        return False

    with open(filename, "r") as file:
        try:
            state = bool(int(file.read()))
        except ValueError:
            # logger.warning("Error reading file")
            state = False
    return state

def write_boolean_to_file(filename: str, state: bool):
    with open(filename, "w") as file:
        file.write(str(int(state)))
