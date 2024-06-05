#!/usr/bin/env python3
'''
basic redis
writing strings to redis
'''
from typing import Union
import uuid
import redis


class Cache():
    '''
    cache class redis
    '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store method
        arguments data
        returns string
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
