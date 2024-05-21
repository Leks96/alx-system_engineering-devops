#!/usr/bin/python3

"""
Python script to export TODO list data for a specified user into a JSON file.
"""

import requests
import sys
import json

def fetch_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    return response.json()

def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()

def find_employee_info(user_id, users):
    user = next((user for user in users if user['id'] == user_id), None)
    return user['username'], user['id'] if user else (None, None)

def main(user_id):
    todos = fetch_todos()
    users = fetch_users()
    username, id_no = find_employee_info(user_id, users)
    
    if not username:
        print(f"No user found with ID {user_id}")
        return
    
    tasks = [
        {
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        }
        for todo in todos if todo['userId'] == user_id
    ]
    
    final_data = {id_no: tasks}
    json_data = json.dumps(final_data, indent=4)
    
    filename = f"{user_id}.json"
    with open(filename, "w") as file:
        file.write(json_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <user_id>")
        sys.exit(1)
    
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("User ID must be an integer")
        sys.exit(1)
    
    main(user_id)
