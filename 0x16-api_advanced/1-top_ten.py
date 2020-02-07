#!/usr/bin/python3
"""Return the number of subscribers to a subreddit"""
import requests
from sys import argv


def top_ten(subreddit):
    p = {"limit": 10}
    url = "https://reddit.com/r/" + subreddit + "/hot.json"
    ua = {'User-agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=ua, params=p)
    data = resp.json().get("data", {})
    l = data.get("children", [])
    for x in l:
        print(x.get("data", {}).get("title", ""))
    if len(l) == 0:
        print(None)
