import urllib.request
import json

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.count:v1.0 (by /u/yourusername)"}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                return data['data']['subscribers']
            else:
                return 0
            except:
                return 0                                                                                                                            
