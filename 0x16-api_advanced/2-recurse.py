#!/usr/bin/python3
"""
Function that returns all hot articles
"""
import requests


def recurse(subreddit, next_page="", hot_list=[]):
    """
    return top post
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
            return recurse(subreddit, next_page, hot_list)
        else:
            return hot_list
    else:
        return (None)
