import json


def update_employee_by_id(file, e_id, new_details):
    with open(file, "r") as read_file:
        data = json.load(read_file)

    for employee in data["employee"]:
        if employee["id"] == e_id:
            employee.update(new_details)
            print(f"Employee updated successfully!")
            print(f"Name: {employee['name']}, Email: {employee['email']}, Dept: {employee['dept']}, Age: {employee['age']}")
            break
    else:
        print(f"Employee with id: {e_id} not found!")

    with open(file, "w") as updated_file:
        json.dump(data, updated_file, indent=4)
