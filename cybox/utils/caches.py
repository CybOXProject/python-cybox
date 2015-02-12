# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


class CacheMiss(Exception):
    """Item was not found in a cache."""
    pass


class Cache(object):
    """Abstract class for storing and retrieving Objects and Observables."""

    def put(self, value, id_=None):
        """Save a value in the cache.

        If `id_` is provided, this is the key used to save the item.
        Otherwise, if `value` has an `id_` attribute, it is used.
        Lastly, if no other ID can be determined, the cache provider is
        responsible for generating one.
        """

        if not id_:
            try:
                id_ = value.id_
            except AttributeError:
                id_ = self._generate_id()

        return self._save(value, id_)

    def _generate_id(self):
        raise NotImplementedError

    def _save(self, value, id_):
        """Private function to actually save the item.

        In some cases, the ID is determined in this step, so return it to the
        caller
        """
        raise NotImplementedError

    def get(self, id_):
        """Retrieve a value from the cache"""
        raise NotImplementedError

    def count(self):
        """Return number of items in the cache"""
        raise NotImplementedError

    def clear(self):
        """Clear all items from the cache"""
        pass


class DictCache(Cache):

    def __init__(self):
        self.__inner = {}
        self._next_id = 0

    def _generate_id(self):
        # Find and unused integer ID. Note that this might not
        # correspond to the actual order items were entered
        while self._next_id in self.__inner:
            self._next_id += 1
        return self._next_id

    def _save(self, value, id_):
        self.__inner[id_] = value
        return id_

    def get(self, id_):
        try:
            return self.__inner[id_]
        except KeyError:
            raise CacheMiss

    def count(self):
        return len(self.__inner)

    def clear(self):
        self.__inner = {}
        # No need to reset _next_id


# Singleton instance within this module. It is lazily instantiated, so simply
# importing the utils module will not create the object.
__cache = None


def _get_cache():
    """Return the `cybox.utils` module's global cache object.

    Only under rare circumstances should this function be called by external
    code. More likely, external code should initialize its own Cache object.

    The implicit, built-in global cache is used when parsing XML or JSON
    representations and dealing with internal references within a document.
    """
    global __cache
    if not __cache:
        __cache = DictCache()
    return __cache


def cache_put(value, id_=None):
    """Save a value in the global cache"""
    new_id = _get_cache().put(value, id_)
    return new_id


def cache_get(id_):
    """Retrieve a value from the global cache"""
    return _get_cache().get(id_)


def cache_count():
    """Get the number of items in the global cache"""
    return _get_cache().count()


def cache_clear():
    """Clear the global cache"""
    _get_cache().clear()
