#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:app_charis:1.0.0 (by /u/charis)'}

    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()['data']['children']
        lim = 10
        for post in data:
            lim -= 1
            if lim <= 0:
                return
            print(post['data']['title'])

    except Exception:
        print(None)
        return
