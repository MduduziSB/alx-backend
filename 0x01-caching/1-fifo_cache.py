#!/usr/bin/env python3
"""LIFO module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Assigns item value to the dictionary
        for the given key using FIFO algorithm
        """
        if key is not None and item is not None:
            if key is not None and item is not None:
                self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.keys.pop(0)
                del self.cache_data[discard_key]
                print('DISCARD: {:s}'.format(discard_key))

    def get(self, key):
        """ Returns the value linked to the key in self.cache_data """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
