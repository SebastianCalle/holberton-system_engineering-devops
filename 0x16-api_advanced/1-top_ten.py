#!/usr/bin/python3
"""
Function that returns 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Print top ten post
    """
    headers = {'User-agent': '/u/Api advance project'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        list_post = res.json()['data']['children']
        for post in list_post:
            print(post['data']['title'])
    else:
        print(None)
