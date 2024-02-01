#!/usr/bin/env python3
"""LIFOCache Module"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class definition"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add key/value pair to cache data."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discarded_key = self.keys.pop(-2)
                print(f"DISCARD: {discarded_key}\n")

    def get(self, key):
        """ Returns the value linked to the key in self.cache_data """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
