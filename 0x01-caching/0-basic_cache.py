#!/usr/bin/env python3
"""class BasicCache that inherits from BaseCaching and is a caching system
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ - dictionary from the parent class BaseCaching
    """
    def put(self, key, item):
        """assign to the dictionary to cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return the value in cache
        """
        return self.cache_data.get(key, None)
