#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import requests
import redis
from functools import wraps
from typing import Callable


cache = redis.Redis()


@count_calls
def get_page(url: str) -> str:
    """ obtains HTML content of a particular URL
    Return:
        The HTML content
    """
    return requests.get(url).text


def count_calls(fn: Callable) -> Callable:
    """ counts how many time a function is called """
    @wraps(fn)
    def wrapper(*args, **kwargs) -> str:
        """ moke function """
        key = 'count:' + args[0]
        cache.incr(key)
        cache.setex(key, 10, args[0])
        return fn(*args, **kwargs)
    return wrapper
