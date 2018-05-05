#!/usr/bin/python3
""" 2 - gather data from reddit """
import requests



def recurse(subreddit, nextPage=None, hot=[]):
    urll = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if nextPage:
        url = url + "?after={}".format(nextPage)

    response = requests.get(url, allow_redirects=False).json()

    if "data" not in response:
        return None

    if "children" in response['data']:
        for child in response['data']['children']:
            hot.append(child['data']['title'])
    
    if response['data']['after'] is not None:
        return recurse(subreddit, nextPage=res['data']['after'], hot=hot)
    else:
        return hot
