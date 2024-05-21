#!/usr/bin/python3

"""
Python script to fetch and display the TODO list progress of an employee based on their ID using a REST API.
"""

import requests
import sys

def fetch_todos(user_id):
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = todos_response.json()
    completed_tasks = [task for task in todos if task['userId'] == user_id and task['completed']]
    return todos, completed_tasks

def fetch_employee_name(user_id):
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()
    user = next((user for user in users if user['id'] == user_id), None)
    return user['name'] if user else None

def main(user_id):
    todos, completed_tasks = fetch_todos(user_id)
    employee_name = fetch_employee_name(user_id)
    
    if not employee_name:
        print(f"No employee found with ID {user_id}")
        return

    total_tasks = len([task for task in todos if task['userId'] == user_id])
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)
    
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    main(user_id)
