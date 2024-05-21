#!/usr/bin/python3

"""
Python script to export TODO list data for a specified user into a CSV file.
"""

import requests
import sys
import csv

def fetch_todos():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    return response.json()

def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()

def find_employee_username(user_id, users):
    user = next((user for user in users if user['id'] == user_id), None)
    return user['username'] if user else None

def write_to_csv(user_id, username, todos):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo['userId'] == user_id:
                writer.writerow([todo['userId'], username, todo['completed'], todo['title']])

def main(user_id):
    todos = fetch_todos()
    users = fetch_users()
    username = find_employee_username(user_id, users)
    
    if not username:
        print(f"No user found with ID {user_id}")
        return
    
    write_to_csv(user_id, username, todos)

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
