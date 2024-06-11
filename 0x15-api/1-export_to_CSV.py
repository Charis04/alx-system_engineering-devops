#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys
    import urllib

    if len(sys.argv) < 2:
        exit
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    res = requests.get(f"{url}users/{employee_id}")
    employee_name = res.json()['name']

    # get tasks
    res = requests.get(f"{url}todos")
    tasks = res.json()
    T_tasks = 0
    C_tasks = 0
    completed = []
    user_data = []
    for task in tasks:
        if task['userId'] == employee_id:
            user_data.append(
                {"USER_ID": employee_id,
                 "USERNAME": employee_name,
                 "TASK_COMPLETED_STATUS": task['completed'],
                 "TASK_TITLE": task['title'],
                 }
                 )
            T_tasks += 1

    filename = f"{employee_id}.csv"
    with open(filename, "w", encoding="utf-8", newline="") as csvfile:
        fieldnames = list(user_data[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(user_data)
