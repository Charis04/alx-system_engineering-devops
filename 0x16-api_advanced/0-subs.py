#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'your_user_agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # response.raise_for_status()

        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException:
        return 0
