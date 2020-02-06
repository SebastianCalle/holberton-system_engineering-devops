#!/usr/bin/python3
"""
Function that returns 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Return number of subscribers
    """
    headers = {'User-agent': '/u/Api advance project'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        list_post = res.json()['data']['children']
        i = 0
        while i < 9:
            print(list_post[i]['data']['title'])
            i += 1
    else:
        return 0
