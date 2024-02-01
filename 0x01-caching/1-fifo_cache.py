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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, discard the first item (FIFO)
                discarded_key, _ = next(iter(self.cache_data.items()))
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}\n")

            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to the key in self.cache_data """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
