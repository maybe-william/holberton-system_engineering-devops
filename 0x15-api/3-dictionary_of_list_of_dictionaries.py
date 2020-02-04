#!/usr/bin/python3
"""Export data about all users and tasks to json"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    resp = requests.get(url)
    users = resp.json()
    my_json = {}
    for user in users:
        user_id = str(user.get("id"))
        url = "https://jsonplaceholder.typicode.com/todos?userId=" + user_id
        resp = requests.get(url)
        tasks = resp.json()

        username = user.get("username")

        new_tasks = []
        new_task = {}
        for task in tasks:
            new_task["task"] = task.get("title")
            new_task["completed"] = task.get("completed")
            new_task["username"] = username
            new_tasks.append(new_task)
            new_task = {}

        my_json[user_id] = new_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(my_json, f)
