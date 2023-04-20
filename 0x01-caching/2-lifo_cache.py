#!/usr/bin/env python3
"""LIFOCache Class Module
LIFOCache is a caching replacement policy that removes the
the last item in a cache when it is full
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache: Inherits from BaseCaching and is a
    caching system
    """
    def __init__(self):
        """
        init of the Class
        """
        super().__init__()
        self.count = 0

    def put(self, key, item):
        """Stores a key-value pair in the cache_data dictionary
        but, discards the last key-value pair when the cache is full.

        The cache has a size of 4
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = list(self.cache_data.keys())[-2 + self.count]
                del self.cache_data[last_item]
                print(f'DISCARD: {last_item}')
                if (self.count == -1):
                    self.count = 0
                else:
                    self.count -= 1

    def get(self, key):
        """Returns the value linked to a key from the cache
        """
        return self.cache_data.get(key)
