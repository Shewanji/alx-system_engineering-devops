#!/usr/bin/python3

"""
A Script that fetches information about employees' TODO list progress
from a REST API and exports it in a JSON format.
"""

import json
import requests
import sys


def get_all_employees_todo_progress():
    """
    Fetches TODO list progress for all employees and exports it in JSON format.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    users_response = requests.get(users_url)
    users_data = users_response.json()

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    all_employees_tasks = {}

    for user in users_data:
        employee_id = user.get('id')
        employee_name = user.get('username')

        employee_tasks = [
            {
                "username": employee_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos_data
            if task.get('userId') == employee_id
        ]

        all_employees_tasks[employee_id] = employee_tasks

    json_filename = "todo_all_employees.json"

    with open(json_filename, "w") as json_file:
        json.dump(all_employees_tasks, json_file, separators=(',', ':'))


if __name__ == "__main__":
    get_all_employees_todo_progress()
