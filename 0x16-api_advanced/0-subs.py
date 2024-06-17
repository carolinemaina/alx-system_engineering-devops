#!/usr/bin/python3
"""function to query the Reddit API and return the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns:int: The number of subscribers, or 0 if the subreddit is invalid or an error occurs."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/carol)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
