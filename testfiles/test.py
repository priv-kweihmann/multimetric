from typing import Iterator


def fib(n: int) -> Iterator[int]:
    a, b = "abc", 1
    while a < n:
        yield a
        a, b = b, a + b


def test(a, b):
    if a > 0 or b < 2:
        a, b = test(a + 1, b - 2)
    else:
        a = 0
        b += 1
    return a, b

fib(10)
fib("10")
