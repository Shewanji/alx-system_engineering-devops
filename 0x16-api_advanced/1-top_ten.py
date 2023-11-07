#!/usr/bin/python3
"""module queries the Reddit API"""

import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User-Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
    else:
        print(None)
