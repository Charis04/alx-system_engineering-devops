#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java should
not).
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and counts the occurrences of specified keywords.

    Args:
    subreddit (str): The name of the subreddit to query.
    word_list (list of str): A list of keywords to count in the titles.
    after (str): The "after" parameter used for pagination (used in recursion).
    word_count (dict): Dictionary to hold the count of keywords (used in
    recursion).

    Returns:
    None: Prints the sorted count of keywords.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        articles = data['data']['children']

        # Convert word_list to lowercase for case-insensitive matching
        word_list = [word.lower() for word in word_list]

        for article in articles:
            title = article['data']['title'].lower().split()

            # Count occurrences of each keyword in the title
            for word in word_list:
                word_count[word] = word_count.get(word, 0) + title.count(word)

        # Check if there is a next page
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            # Sort and print results after recursion is done
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")

    except requests.RequestException:
        return
