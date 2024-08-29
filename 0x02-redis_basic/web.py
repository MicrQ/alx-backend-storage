#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import requests
import redis
from functools import wraps
from typing import Callable


cache = redis.Redis()


def count_calls(fn: Callable) -> Callable:
    """ counts how many time a function is called """
    @wraps(fn)
    def wrapper(*args, **kwargs) -> str:
        """ moke function """
        key = 'count:' + args[0]
        cache.incr(key)
        result = fn(*args, **kwargs)
        return result
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """ obtains HTML content of a particular URL
    Return:
        The HTML content
    """
    res = cache.get(url)
    if res:
        return res.decode('utf-8')

    res = requests.get(url).text
    cache.setex(url, 10, res)
    return res
