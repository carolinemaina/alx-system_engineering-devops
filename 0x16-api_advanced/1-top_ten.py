#!/usr/bin/python3
"""
This module contains a function to print the titles of the first 10 hot posts
from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "python: top_ten.posts: v1.0"
                          "(by /u/yourusername)"
            }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for i, post in enumerate(posts[:10]):
                print(post.get('data', {}).get('title', ''))
        else:
            print(None)
    except requests.RequestException:
        print(None)
