#!/usr/bin/python3
'''convert to json format'''

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]

    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos?userId={}".format(userId)).json()

    with open("{}.json".format(userId), 'w+') as f:
        json.dump({
            userId: [{
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": user['name']
                } for todo in todos
            ]
        }, f)
