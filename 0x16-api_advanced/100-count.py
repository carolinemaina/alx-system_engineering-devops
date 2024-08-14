#!/usr/bin/python3
"""
This module contains a recursive function to count and print occurrences of
keywords in hot article titles from a given subreddit using the Reddit API.
"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """Recursively fetches hot articles and counts keyword occurrences."""
    if hot_list is None:
        hot_list = []
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {
                "User-Agent": "python: count_words: v1.0 (by /u/yourusername)"
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
                        title = post.get('data', {}).get('title', '')
                        hot_list.append(title.lower())
                    next_after = data.get('data', {}).get('after')
                    if next_after:
                        return count_words(
                                subreddit,
                                word_list,
                                hot_list,
                                next_after
                                )
                    else:
                        return count_keywords(word_list, hot_list)
                else:
                    return count_keywords(word_list, hot_list)
            else:
                return None
        except requests.RequestException:
            return None


def count_keywords(word_list, hot_list):
    """Counts occurrences of each keyword in the
    hot_list and prints results."""
    all_titles = ' '.join(hot_list)
    words = re.findall(r'\b\w+\b', all_titles)
    word_count = Counter(words)
    word_list = [word.lower() for word in word_list]
    results = {}
    for word in word_list:
        if word in word_count:
            results[word] = word_count[word]
    sorted_results = sorted(
            results.items(),
            key=lambda item: (-item[1], item[0])
            )

    for word, count in sorted_results:
        print(f"{word}: {count}")
    return None
