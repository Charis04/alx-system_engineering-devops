#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    import urllib

    if len(sys.argv) < 2:
        exit
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    res = requests.get(f"{url}users/{employee_id}")
    employee_name = res.json()['username']

    # get tasks
    res = requests.get(f"{url}todos")
    tasks = res.json()
    user_data = {employee_id: []}
    for task in tasks:
        if task['userId'] == int(employee_id):
            user_data[employee_id].append(
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": employee_name
                }
            )

    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as jf:
        json.dump(user_data, jf)
