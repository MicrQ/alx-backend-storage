#!/usr/bin/env python3
"""  """
import redis
from typing import Union
import uuid
from functools import wraps


def count_calls(method: callable) -> callable:
    """ counts number of calls to the Cache class methods """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ mock method """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """ redis implemetation """
    def __init__(self):
        """ initializes private redis instance named _redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            stores {data} in Redis using random uuid key
        Return:
            (str) the key (random uuid)
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: callable = None) -> Union[str, bytes, int, float]:
        """ retrieves {key} from Redis and returns it """
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """ returns the value of the key """
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """ returns the value of the key """
        return self.get(key, int)
