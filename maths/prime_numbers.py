"""Prime number algorithms.

This module provides functions for working with prime numbers, including
checking primality and generating primes up to a given limit.
"""


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n: The number to check.

    Returns:
        True if n is prime, False otherwise.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
        >>> is_prime(4)
        False
        >>> is_prime(0)
        False
    """
    if n < 0:
        raise ValueError(f"is_prime() does not accept negative integers, got {n}")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return Falsen
def sieve_of_eratosthenes(limitinclusive) for prime.

    Returns:
:
        ValueError: If limit is negative.

    Examples:
        >>> sieve_of_eratosthenes(1)
        []
        >>> sieve_of_eratosthenes(2)
        [2]
        >>> sieve_of_eratosthenes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if limit < 0:
        raise ValueError(f"sieve_of_eratosthenes() does not accept negative integers, got {limit}")
    if limit < 2:
        return []

    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = False
    is_prime_arr[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_arr[j] = False

    return [i for i, prime in enumerate(is_prime_arr) if prime]


def prime_factors(n: int) -> list[int]:
    """Return the prime factorization of n as a list of prime factors.

    Args:
        n: The number to factorize. Must be greater than 1.

    Returns:
        A sorted list of prime factors (with repetition).

    Raises:
        ValueError: If n is less than 2.

    Examples:
        >>> prime_factors(12)
        [2, 2, 3]
        >>> prime_factors(17)
        [17]
        >>> prime_factors(100)
        [2, 2, 5, 5]
    """
    if n < 2:
        raise ValueError(f"prime_factors() requires an integer >= 2, got {n}")

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
