#!/usr/bin/python3
'''convert to csv format'''

if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]

    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos?userId={}".format(userId)).json()

    with open("{}.csv".format(userId), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([id, user['name'], todo['completed'], todo['title']])
