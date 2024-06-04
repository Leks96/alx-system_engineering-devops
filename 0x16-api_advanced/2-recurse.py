#!/usr/bin/python3
import requests
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

def recurse(subreddit, hot_list=None):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    if hot_list is None:
        hot_list = []
        
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        
        if children:
            for post in children:
                title = post.get("data", {}).get("title")
                hot_list.append(title)
            
            after = data.get("after")
            if after:
                params["after"] = after
                recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None