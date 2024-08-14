#!/usr/bin/python3
"""
This module contains a recursive function to fetch all hot article titles
from a given subreddit using the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively fetches all hot articles for a given subreddit."""
    if hot_list is None:
        hot_list = []
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {
                "User-Agent": "python: recurse.hot_articles: v1.0"
                "(by /u/yourusername)"
                }
        params = {'after': after} if after else {}
        try:
            response = requests.get(
                    url,
                    headers=headers,
                    params=params,
                    allow_redirects=False
                    )
            if response.status_code == 200:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                if posts:
                    for post in posts:
                        hot_list.append(post.get('data', {}).get('title', ''))
                    next_after = data.get('data', {}).get('after')
                    if next_after:
                        return recurse(subreddit, hot_list, next_after)
                    else:
                        return hot_list
                else:
                    return hot_list
            else:
                return None
        except requests.RequestException:
            return None
