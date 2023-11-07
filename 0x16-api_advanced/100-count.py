#!/usr/bin/python3
"""module that queries the Reddit API"""

import requests


def count_words(subreddit, word_list):
    """
    recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces. Javascript should
    count as javascript, but java should not).
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Custom User-Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            word_dict = {word.lower(): 0 for word in word_list}
            after = data["data"]["after"]
            while after:
                for post in data["data"]["children"]:
                    title = post["data"]["title"].lower()
                    for word in word_list:
                        if word.lower() in title:
                            word_dict[word.lower()] += 1
                url = (f"https://www.reddit.com/r/{subreddit}/hot.json"
                       f"?limit=100&after={after}")
                response = requests.get(url, headers=headers)
                data = response.json()
                if "data" in data:
                    after = data["data"]["after"]
                else:
                    after = None
            sorted_words = sorted(word_dict.items(),
                                  key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")
        else:
            print(None)
    else:
        print(None)
