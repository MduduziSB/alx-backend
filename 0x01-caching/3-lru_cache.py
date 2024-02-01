#!/usr/bin/env python3
"""LRUCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assigns item value to the dictionary
        for the given key using LRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}\n")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Returns the value linked to the key in self.cache_data
        and updates usage order
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
