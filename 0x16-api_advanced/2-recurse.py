#!/usr/bin/python3
"""module that that queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
     recursive function that queries the Reddit API and returns a
     list containing the titles of all hot articles for a given subreddit.
     If no results are found for the given subreddit,
     the function should return None.
     """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Custom User-Agent'}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [post["data"]["title"] for post in data["children"]]
        after = data["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
