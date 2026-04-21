"""Fibonacci sequence implementations using different approaches."""

from functools import lru_cache


def fibonacci_recursive(n: int) -> int:
    """Return the nth Fibonacci number using recursion with memoization.

    >>> fibonacci_recursive(0)
    0
    >>> fibonacci_recursive(1)
    1
    >>> fibonacci_recursive(10)
    55
    >>> fibonacci_recursive(20)
    6765
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    @lru_cache(maxsize=None)
    def _fib(k: int) -> int:
        if k <= 1:
            return k
        return _fib(k - 1) + _fib(k - 2)

    return _fib(n)


def fibonacci_iterative(n: int) -> int:
    """Return the nth Fibonacci number using an iterative approach.

    >>> fibonacci_iterative(0)
    0
    >>> fibonacci_iterative(1)
    1
    >>> fibonacci_iterative(10)
    55
    >>> fibonacci_iterative(20)
    6765
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(limit: int) -> list[int]:
    """Return a list of Fibonacci numbers up to (but not exceeding) limit.

    >>> fibonacci_sequence(0)
    [0]
    >>> fibonacci_sequence(1)
    [0, 1, 1]
    >>> fibonacci_sequence(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    if limit < 0:
        raise ValueError("limit must be a non-negative integer")
    sequence = [0, 1]
    while True:
        next_val = sequence[-1] + sequence[-2]
        if next_val > limit:
            break
        sequence.append(next_val)
    return sequence if limit >= 1 else [0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # Print first 40 numbers to better observe exponential growth
    print("First 40 Fibonacci numbers:")
    for i in range(40):
        print(f"  fib({i}) = {fibonacci_iterative(i)}")
