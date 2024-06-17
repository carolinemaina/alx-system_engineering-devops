#!/usr/bin/python3
"""subscriber count"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            'User-Agent': '"MyRedditSubCounter/1.0 (by /u/rije1)"'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0
