import functools


def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(x):
        key = x
        if key not in cache:
            cache[key] = func(x - 1) + func(x - 2)
        return cache[key]
    return inner
