
import functools

from slowburn import serdes
from slowburn.storage import CacheMissError, _cache_get, _cache_set


__all__ = [
    "cache",
    "cache_factory",
]


def cache_get(cache_name, key):
    key = serdes.serialize(key)
    return serdes.deserialize(_cache_get(cache_name, key))


def cache_set(cache_name, key, value):
    key = serdes.serialize(key)
    value = serdes.serialize(value)
    return _cache_set(cache_name, key, value)


def _cache(func, cache_name):

    def wrapper(*args, **kwargs):
        key = (args, kwargs)

        try:
            out = cache_get(cache_name, key)
        except CacheMissError:
            out = func(*args, **kwargs)
            cache_set(cache_name, key, out)

        return out
    return wrapper


def cache(func):
    return _cache(func, func.__name__)


def cache_factory(cache_name):
    if not isinstance(cache_name, str):
        raise RuntimeError("cache_factory must be called with a string argument (e.g. @cache_factory('foo'))")
    return functools.partial(_cache, cache_name=cache_name)
