#!/usr/bin/env python3
"""FIFOCache Class Module
FIFOCache is a caching replacement policy that removes the
the first item in a cache when it is full
"""
from base_cache import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache: Inherits from BaseCaching and is a
    caching system
    """
    def __init__(self):
        """
        init of the Class
        """
        super().__init__()

    def put(self, key, item):
        """Stores a key-value pair in the cache_data dictionary
        but, discards the first key-value pair when the cache is full.

        The cache has a size of 4
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = list(self.cache_data.keys())[0]
                del self.cache_data[first_item]
                print(f'DISCARD: {first_item}')

    def get(self, key):
        """Returns the value linked to a key from the cache
        """
        return self.cache_data.get(key)
