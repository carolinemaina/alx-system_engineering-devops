#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, count={}):
    if not word_list:
        sorted_counts = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    data = response.json()
    posts = data["data"]["children"]

    for post in posts:
        title = post["data"]["title"]
        for word in word_list:
            if word.lower() in title.lower().split():
                count[word] = count.get(word, 0) + 1

    after = data["data"]["after"]
    count_words(subreddit, word_list, after, count)
