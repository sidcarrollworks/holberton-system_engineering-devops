#!/usr/bin/python3
''' get top 10 '''
import requests


def top_ten(subreddit):
    ''' top ten '''

    url = "https://api.reddit.com/r/{}/hot/".format(subreddit)
    header = {'User-Agent':  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; \
            rv:60.0) Gecko/20100101 Firefox/60.0'}

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        try:
            posts = response.json()["data"]["children"]
            res = ""
            for x in range(10):
                title = posts[x]["data"]["title"]
                res += "{}\n".format(title)
        except:
            res = "None\n"
    print(res, end="")
