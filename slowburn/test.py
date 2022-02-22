
from slowburn.cachetools import cache, cache_factory


def test():

    @cache_factory
    def f(n):
        import time
        time.sleep(1)
        return n + 5

    print(f(1))
    print(f(1))
    print(f(1))
    print(f(2))


def test2():
    import random

    @cache
    def s(n):
        import time
        time.sleep(n // 2)
        return n

    for i in range(1000):
        n = random.randint(1, 10)
        out = s(n)
        print(out, type(out))
