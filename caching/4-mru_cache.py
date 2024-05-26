#!/usr/bin/env python3
'''
Create a class MRUCache that inherits
from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    MRU class implemtn
    args basecaching class
    '''
    def __init__(self):
        self.stack = []
        super().__init__()

    def put(self, key, item):
        '''
        assigns item to dictionary
        '''
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''
        gets value of cache
        '''
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
