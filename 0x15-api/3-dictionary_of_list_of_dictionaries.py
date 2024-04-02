#!/usr/bin/python3
"""a script that extends your Python script
to export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    users = res.json()

    dict = {}
    for u in users:
        user_id = u.get('id')
        UserName = u.get('username')
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        url = url + '/todos/'
        res = requests.get(url)
        tasks = res.json()
        dict[user_id] = []
        for t in tasks:
            TASK_COMPLETED_STATUS = t.get('completed')
            TASK_TITLE = t.get('title')
            dict[user_id].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": UserName
            })
            with open('todo_all_employees.json', 'w') as f:
                json.dump(dict, f)
