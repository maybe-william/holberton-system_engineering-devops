#!/usr/bin/python3
"""Return the number of subscribers to a subreddit"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    url = "https://reddit.com/r/" + subreddit + "/about.json"
    ua = {'User-agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=ua)
    data = resp.json().get("data", {"subscribers": 0})
    subs = data.get("subscribers", 0)
    return subs
