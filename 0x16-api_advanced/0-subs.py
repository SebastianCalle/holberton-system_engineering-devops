#!/usr/bin/python3
"""
Function that returns number of subscribers
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    Return number of subscribers
    """
    headers = {'User-agent': '/u/Api advance project'}
    client = requests.session()
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = client.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get('data').get('subscribers')
        return data
    else:
        return 0
