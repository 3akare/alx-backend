#!/usr/bin/env python3
"""
LRU Class Module
"""

from base_caching import BaseCaching
from collections import deque

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.key_order = deque()
    
    def get(self, key):
        return self.cache_data.get(key)
    
    def put(self, key, item):
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            oldest_key = self.key_order.popleft()
            del self.cache_data[oldest_key]
            print(f'DISCARD {oldest_key}')

        self.cache_data[key] = item

        if key in self.key_order:
            self.key_order.remove(key)
        self.key_order.append(key)


my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()