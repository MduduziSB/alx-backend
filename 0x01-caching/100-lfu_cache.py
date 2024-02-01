#!/usr/bin/env python3
"""LFUCache Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching """

    def __init__(self):
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """
        Assigns item value to the dictionary
        for the given key using LFU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = []
                min_frequency = min(self.frequency.values())

                for k, v in self.frequency.items():
                    if v == min_frequency:
                        lfu_keys.append(k)

                if len(lfu_keys) > 1:
                    lfu_lru_key = min(
                        self.usage_order,
                        key=lambda k: self.usage_order.index(k)
                    )

                    lfu_keys = [lfu_lru_key]

                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}\n")

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Updates LFU information
        Returns the value linked to the key in self.cache_data
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
