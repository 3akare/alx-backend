#!/usr/bin/env python3
'''BasicCache Class module'''

from typing import Union
from base_cache import BaseCaching


class BasicCache(BaseCaching):
    '''
    BasicCache: Inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        '''Inherits all the properties and methods of BaseCaching'''
        super().__init__()

    def put(self, key: Union[None, int, float, str], item: Union[None, int, float, str]) -> None:  # noqa
        '''Stores a key-value pair in the cache_data dictionary'''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key: Union[None, int, float, str]) -> Union[None, int, float, str]:  # noqa
        '''Retrieves a key-value pair from the cache_data dictionary'''
        if key is None:
            return None
        return self.cache_data.get(key)
