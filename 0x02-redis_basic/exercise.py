#!/usr/bin/env python3
"""
Redis basic.
"""
from typing import Union, Callable, Optional
from functools import wraps
import redis
import uuid


class Cache(object):
    """Cache class to handle redis operations."""
    def __init__(self):
        """stores an instance of the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes and stores a data argument and returns a string."""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
