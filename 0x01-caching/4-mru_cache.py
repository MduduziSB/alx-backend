#!/usr/bin/env python3
"""MRUCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assigns item value to the dictionary
        for the given key using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}\n")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Returns the value linked to the key in self.cache_data"""
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
