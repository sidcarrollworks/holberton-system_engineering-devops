#!/usr/bin/python3
'''convert to json format'''

if __name__ == "__main__":
    import requests
    import json

    url = "https://jsonplaceholder.typicode.com/"
    allTasks = {}
    users = requests.get(url + "users").json()

    for user in users:
        todos = requests.get(url + "todos?userId={}".format(user['id'])).json()
        allTasks[user['id']] = [{
                "username": user['name'],
                "task": todo['title'],
                "completed": todo['completed']
            } for todo in todos
        ]

    with open("todo_all_employees.json", 'w') as f:
        json.dump(allTasks, f)
