#!/usr/bin/python3
''' get number of subs '''
import requests


def number_of_subscribers(subreddit):
    ''' NUM OF SUBS '''
    if type(subreddit) is not str:
        return 0

    header = {'User-Agent': '(DreamPassport/3.0; isao/MyDiGiRabi)'}
    url = "https://api.reddit.com/r/{}/about/".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        try:
            subs = response.json()["data"]["subscribers"]
        except:
            return 0
    else:
        return 0
    return subs
