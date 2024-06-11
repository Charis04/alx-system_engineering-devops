#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":
    import sys
    import urllib
    import requests

    if len(sys.argv) < 2:
        exit
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    res = requests.get(f"{url}users/{employee_id}")
    employee_name = res.json()['name']

    # get tasks
    res = requests.get(f"{url}todos")
    tasks = res.json()
    T_tasks = 0
    C_tasks = 0
    completed = []
    for task in tasks:
        if task['userId'] == int(employee_id):
            T_tasks += 1
            if task['completed']:
                completed.append(task['title'])
                C_tasks += 1

    print(f"Employee {employee_name} is done with tasks({C_tasks}/{T_tasks}):")
    for task in completed:
        print(f"\t {task}")
