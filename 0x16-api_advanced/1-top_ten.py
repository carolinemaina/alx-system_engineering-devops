#!/usr/bin/python3
""" Working with Advanced APIs """

import requests


def top_ten(subreddit):
    if subreddit is None:
        return None
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
            'User-Agent': '"MyRedditSubCounter/1.0 (by /u/rije1)"'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json()
                posts = data['data']['children']
                titles = [post['data']['title'] for post in posts]
            except (Exception, json.JSONDecodeError) as e:
                print(None)
                return
            top_10_titles = titles[:10]
            for title in top_10_titles:
                print(title)
        else:
            return None
    except (Exception, json.JSONDecodeError) as e:
        return None
