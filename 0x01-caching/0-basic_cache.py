#!/usr/bin/env python3
"""BasicCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""

    def put(self, key, item):
        """ Assigns item value to the dictionary for the given key """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to the key in self.cache_data """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
