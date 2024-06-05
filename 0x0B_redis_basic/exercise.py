#!/usr/bin/env python3
'''
basic redis
writing strings to redis
'''
from typing import Callable, Union
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
    
    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        '''
        method to retrieve data and turn to python
        '''
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        '''
        transform redis var to python str
        '''
        variable = self._redis.get(key)
        return variable.decode('utf-8')
    
    def get_int(self, key: str) -> int:
        '''
        transform redis var to python str
        '''
        variable = self._redis.get(key)
        try:
            variable = int(variable.decode('utf-8'))
        except Exception:
            variable = 0
        return variable
