#!/usr/bin/env python3
'''
basic redis
writing strings to redis
'''
from typing import Callable, Union
import uuid
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
    decorator taking single method arg, returns callable
    '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        increments count each time method is called and returns value
        '''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    '''
    stores history of inputs outputs
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        saves input output of functions in redis
        '''
        inputKey = method.__qualname__ + ':inputs'
        outputKey = method.__qualname__ + ':outputs'
        output = method(self, *args, **kwargs)
        self._redis.rpush(inputKey, str(args))
        self._redis.rpush(outputKey, str(output))
        return output
    return wrapper

def replay(fn: Callable):
    '''
    displays the call history of a certain fucntion
    '''
    r = redis.Redis()
    fName = fn.__qualname__
    nCalls = r.get(fName)
    try:
        nCalls = nCalls.decode('utf-8')
    except Exception:
        nCalls = 0
    print(f'{fName} was called {nCalls} times:')
    ins = r.lrange(fName + ':inputs', 0, -1)
    outs = r.lrange(fName + ':outputs', 0, -1)
    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ''
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ''
        print(f'{fName}(*{i}) -> {o}')


class Cache():
    '''
    cache class redis
    '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
