#!/usr/bin/python3
"""
Test
"""
import sys

try:
    BasicCache = __import__('0-basic_cache').BasicCache
    BaseCaching = __import__('base_caching').BaseCaching
    if issubclass(BasicCache, BaseCaching):
        print("OK")
    else:
        print("BasicCache doesn't inherit from BaseCaching")
except:
    print(sys.exc_info()[1])