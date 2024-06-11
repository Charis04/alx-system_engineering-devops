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
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    res = requests.get(f"{url}users/{employee_id}")
    employee_name = res.json()['username']

    # get tasks
    res = requests.get(f"{url}todos")
    tasks = res.json()
    T_tasks = 0
    C_tasks = 0
    user_data = []
    for task in tasks:
        if task['userId'] == int(employee_id):
            user_data.append(
                [employee_id, employee_name, task['completed'], task['title']]
                )
            T_tasks += 1

    filename = f"{employee_id}.csv"
    with open(filename, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in user_data:
            writer.writerow([str(item) for item in row])
