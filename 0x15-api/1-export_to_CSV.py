#!/usr/bin/python3

"""
This script fetches information about an employee's
TODO list progress from a REST API
and exports it in CSV format.

Requirements:
- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee
  TODO list progress in this format:
  "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv

Usage:
python script.py <EMPLOYEE_ID>
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches employee's TODO list progress and exports it in CSV format.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_id = user_data.get('id')
    employee_name = user_data.get('username')

    todos_response = requests.get(todos_url)
    todo_data = todos_response.json()

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)

        # Initialize task_completed before the loop
        task_completed = False

        for task in todo_data:
            task_id = task.get('id')
            task_title = task.get('title')
            task_completed = task.get('completed', False)

            csv_writer.writerow([
                employee_id,
                employee_name,
                str(task_completed),
                task_title
            ])

    # Check if there are no tasks for the employee
    if not todo_data:
        print(f"No tasks found for employee \
              {employee_name} (ID {employee_id}).")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <EMPLOYEE_ID>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
