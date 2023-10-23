#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

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
    employee_name = user_data.get('name')

    todos_response = requests.get(todos_url)
    todo_data = todos_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get('completed'))

    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task.get('completed'):
            print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <EMPLOYEE_ID>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
