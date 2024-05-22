import json


def delete_employee_by_id(file, e_id):
    with open(file, "r") as read_file:
        data = json.load(read_file)

    employee_count = len(data["employee"])
    data["employee"] = [employee for employee in data["employee"] if employee["id"] != e_id]
    employee_count_after_deletion = len(data["employee"])

    if employee_count_after_deletion < employee_count:
        with open(file, "w") as write_file:
            json.dump(data, write_file, indent=4)
        print(f"Employee with ID: {e_id} has been deleted.")
    else:
        print(f"Employee with id: {e_id} not found!")
