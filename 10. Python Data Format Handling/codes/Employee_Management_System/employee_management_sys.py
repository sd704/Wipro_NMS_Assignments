"""
    Task 2: Employee Data Management System (Using JSON)

    Background:
        A company needs to develop an employee management system to store and manage employee data.
        The system should allow users to add new employees, update existing employee information, delete employees, and generate reports.

    Questions:
        Design a Python program that interacts with a JSON file to perform CRUD (Create, Read, Update, Delete) operations on employee data.
        Implement functions to add new employees, update existing employee information, delete employees by their ID, and retrieve employee details.
        Use JSON format to store employee data in a structured manner, with each employee represented as a JSON object.
"""

import json
import os
from write_json import write_json
from add_employee_by_id import add_employee_by_id
from get_all_employees import get_all_employees
from get_employee_by_id import get_employee_by_id
from update_employee_by_id import update_employee_by_id
from delete_json import delete_json
from delete_employee_by_id import delete_employee_by_id

filename = "employee_data.json"

employee_data = {
    "employee": [
        {"id": 1, "name": "John Smith", "age": 30, "email": "john@xcorp.com", "dept": "HR"},
        {"id": 2, "name": "Jane Doe", "age": 25, "email": "jane@xcorp.com", "dept": "Finance"},
        {"id": 3, "name": "Alice Johnson", "age": 28, "email": "alice@xcorp.com", "dept": "IT"},
        {"id": 4, "name": "Bob Brown", "age": 35, "email": "bob@xcorp.com", "dept": "Marketing"},
        {"id": 5, "name": "Charlie Black", "age": 40, "email": "charlie@xcorp.com", "dept": "Sales"},
        {"id": 6, "name": "Diana Green", "age": 32, "email": "diana@xcorp.com", "dept": "HR"},
        {"id": 7, "name": "Eve White", "age": 27, "email": "eve@xcorp.com", "dept": "Finance"},
        {"id": 8, "name": "Frank Blue", "age": 29, "email": "frank@xcorp.com", "dept": "IT"},
        {"id": 9, "name": "Grace Hopper", "age": 31, "email": "grace@xcorp.com", "dept": "Marketing"},
        {"id": 10, "name": "Hank Purple", "age": 26, "email": "hank@xcorp.com", "dept": "Sales"}
    ]
}

new_employee_data = {
    "id": 13,
    "name": "Anna White",
    "age": 24,
    "email": "anna@xcorp.com",
    "dept": "HR"
}

# write_json(filename, employee_data)
# get_all_employees(filename)
# add_employee_by_id(filename, new_employee_data)
# get_employee_by_id(filename, 13)
# update_employee_by_id(filename, 13, {"name": "Ana White"})
# get_all_employees(filename)
# delete_employee_by_id(filename, 13)
# delete_json(filename)










