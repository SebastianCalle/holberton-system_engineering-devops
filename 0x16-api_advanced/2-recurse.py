#!/usr/bin/python3
"""
Function that returns all hot articles
"""
import requests


def recursive(subreddit, next_page, hot_list=[], i=0):
    """
    Recursive function
    """
    headers = {'User-agent': '/u/Api advance project'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 next_page)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        list_post1 = res.json()['data']['children']
        for post in list_post1:
            hot_list.append(post['data']['title'])
        next_page = res.json()['data']['after']
        if next_page:
            return recursive(subreddit, next_page, hot_list, i+1)
        else:
            return hot_list


def recurse(subreddit):
    """
    return top post
    """
    next_page = ""
    headers = {'User-agent': '/u/Api advance project'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit,
                                             next_page)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        next_page = res.json()['data']['after']
        list_post1 = res.json()['data']['children']
        hot_list = []
        for post in list_post1:
            hot_list.append(post['data']['title'])
        return recursive(subreddit, next_page, hot_list, 1)
    else:
        return (None)
