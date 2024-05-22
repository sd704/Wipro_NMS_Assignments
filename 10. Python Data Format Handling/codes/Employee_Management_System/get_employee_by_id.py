import json


def get_employee_by_id(file, e_id):
    with open(file, "r") as file:
        data = json.load(file)

    employee_found = False
    for employee in data["employee"]:
        if employee["id"] == e_id:
            print(
                f"Name: {employee['name']}, Email: {employee['email']}, Dept: {employee['dept']}, Age: {employee['age']}")
            employee_found = True
            break

    if not employee_found:
        print(f"Employee with id: {e_id} not found!")
