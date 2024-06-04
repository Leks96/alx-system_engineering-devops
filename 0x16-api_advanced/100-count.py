#!/usr/bin/env python3
""" Module for storing the count_words function. """
import requests
from collections import Counter

def count_words(subreddit, word_list, count=None):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    if count is None:
        count = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        
        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            words = title.split()
            for word in words:
                word = word.rstrip(".,!?")
                if word in word_list:
                    count[word] += 1
            
        after = data.get("after")
        if after:
            params["after"] = after
            count = count_words(subreddit, word_list, count)
        
    return count