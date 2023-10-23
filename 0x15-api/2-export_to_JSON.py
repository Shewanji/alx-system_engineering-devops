#!/usr/bin/python3

"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays an employee's TODO list progress.

    Args:
        employee_id (int): The employee ID to fetch data for.

    Returns:
        None
    """

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('username')

    todos_response = requests.get(todos_url)
    todo_data = todos_response.json()

    user_tasks = {
        employee_id: [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name
            } for task in todo_data
        ]
    }

    json_filename = f"{employee_id}.json"

    # Save the JSON file without line breaks and indentation
    json_str = json.dumps(user_tasks, separators=(',', ':'))
    with open(json_filename, 'w') as json_file:
        json_file.write(json_str)

    if not todo_data:
        print(f"No tasks found for employee \
              {employee_name} (ID {employee_id}).")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <EMPLOYEE_ID>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
