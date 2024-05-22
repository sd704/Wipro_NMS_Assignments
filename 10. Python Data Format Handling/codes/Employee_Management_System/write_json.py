import json


def write_json(file, e_data):
    data = e_data

    with open(file, "w") as file:
        json.dump(data, file, indent=4)
