from functools import lru_cache

n, x, y = map(int, input().split())


@lru_cache(maxsize=None)
def f(n, x, y):
    if n <= 1:
        return 0
    else:
        return f(n - 1, x, y) + x * blue(n, x, y)


@lru_cache(maxsize=None)
def blue(n, x, y):
    if n == 1:
        return 1
    else:
        return blue(n - 1, x, y) * y + f(n - 1, x, y)


print(f(n, x, y))
