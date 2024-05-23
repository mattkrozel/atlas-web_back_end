#!/usr/bin/env python3
'''
Create a class BasicCache that inherits
from BaseCaching and is a caching system
'''

from typing import Union
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    '''
    cache class implemtn
    args basecaching class
    '''
    def put(self, key: str, item: str) -> None:
        '''
        adds value in cache
        '''
        if key and item:
            self.cache_data[key] = item


    def get(self, key: str) -> Union[None, object]:
        '''
        gets value of cache
        '''
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
