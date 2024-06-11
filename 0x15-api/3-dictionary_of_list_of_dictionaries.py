#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com/"

    users_res = requests.get(f"{url}users")
    users = users_res.json()
    tasks_res = requests.get(f"{url}todos")
    tasks = tasks_res.json()

    user_data = {}
    for user in users:
        user_data[user['id']] = []
        for task in tasks:
            if task['userId'] == int(user['id']):
                user_data[user['id']].append(
                    {
                        "username": user['username'],
                        "task": task['title'],
                        "completed": task['completed']
                    }
                )

    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as jf:
        json.dump(user_data, jf)
