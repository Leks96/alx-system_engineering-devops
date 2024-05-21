#!/usr/bin/python3

"""
Python script that exports data in JSON format for all employees' TODO lists.
"""

import requests
import json

def fetch_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    return response.json()

def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()

def main():
    todos = fetch_todos()
    users = fetch_users()

    all_todos = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_todos = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user_id
        ]
        all_todos[user_id] = user_todos

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_todos, file, indent=4)

if __name__ == "__main__":
    main()
