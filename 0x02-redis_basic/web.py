#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import requests
import redis


cache = redis.Redis()


def get_page(url: str) -> str:
    """ obtains HTML content of a particular URL
    Return:
        The HTML content
    """
    cache.setex('count:' + url, 10)
    return requests.get(url).text
