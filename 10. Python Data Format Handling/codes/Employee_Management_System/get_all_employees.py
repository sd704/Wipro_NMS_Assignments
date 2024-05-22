import json


def get_all_employees(file):
    with open(file, "r") as file:
        data = json.load(file)
    for employee in data["employee"]:
        print(f"Name: {employee['name']}, Email: {employee['email']}, Dept: {employee['dept']}, Age: {employee['age']}")
