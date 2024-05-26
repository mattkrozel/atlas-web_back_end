#!/usr/bin/env python3
'''
Create a class LRUCache that inherits
from BaseCaching
'''

from typing import Union
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    FIFO class implemtn
    args basecaching class
    '''
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key: str, item: str) -> None:
        '''
        assigns item to dictionary
        '''
        if key and item:
            self.isFillCache(key)
            self.cache_data[key] = item

    def get(self, key: str) -> Union[None, object]:
        '''
        gets value of cache
        '''
        if key not in self.cache_data.keys():
            return None
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data[key]
    
    def isFillCache(self, key) -> None:
        '''
        checking if the cache is full
        '''
        if self.cache_data.get(key):
            self.queue.remove(key)
        self.queue.append(key)
        if len(self.queue) > self.MAX_ITEMS:
            deleted_item = self.queue.pop(0)
            self.cache_data.pop(deleted_item)
            print(f'DISCARD: {deleted_item}')
