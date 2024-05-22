import json


def add_employee_by_id(file, new_employee):
    with open(file, "r") as read_file:
        data = json.load(read_file)

    for employee in data["employee"]:
        if employee["id"] == new_employee["id"]:
            print(f"Employee with ID: {new_employee['id']} already exists.")
            return

    data["employee"].append(new_employee)
    with open(file, "w") as write_file:
        json.dump(data, write_file, indent=4)
    print(f"Employee with ID: {new_employee['id']} has been added successfully.")
