#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): The list that stores the titles of hot articles
    (used in recursion). after (str): The "after" parameter used for
    pagination (used in recursion).

    Returns:
    list: A list of titles of hot articles, or None if the subreddit is
    invalid or no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
        if response.status_code == 200:
            data = response.json()
            articles = data['data']['children']
            for article in articles:
                hot_list.append(article['data']['title'])

            # Check if there is a next page
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
