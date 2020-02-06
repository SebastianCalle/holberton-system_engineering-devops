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
    headers = {'user-agent': '/u/Api advance project'}
    client = requests.session()
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = client.get(url, headers=headers)
    if res.status_code != 200:
        return 200
    data = res.json().get('data').get('subscribers')
    if data:
        return data
    else:
        return 0
