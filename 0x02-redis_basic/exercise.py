#!/usr/bin/env python3
"""  """
import redis
from typing import Union
import uuid


class Cache:
    """ redis implemetation """
    def __init__(self):
        """ initializes private redis instance named _redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            stores {data} in Redis using random uuid key
        Return:
            (str) the key (random uuid)
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
