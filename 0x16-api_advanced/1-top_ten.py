#!/usr/bin/python3

"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        for post in response.json().get("data", {}).get("children", []):
            print(post.get("data", {}).get("title"))
    else:
        print(None)
