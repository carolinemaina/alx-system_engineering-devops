#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python/requests:top_ten:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                posts = data.get("children", [])
                for post in posts:
                    print(post.get("data", {}).get("title"))
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
