#!/usr/bin/python3
"""a script that extends your Python
script to export data in the JSON format."""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    res = requests.get(url_user)
    USERNAME = res.json().get('username')
    url_task = url_user + '/todos'
    res = requests.get(url_task)
    tasks = res.json()

    dict = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME})
    with open('{}.json'.format(USER_ID), 'w') as f:
        json.dump(dict, f)
