#!/usr/bin/python3
"""
Function that returns number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return number of subscribers
    """
    headers = {'User-agent': '/u/Api advance project'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
