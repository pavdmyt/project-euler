"""
Some helper functions.
"""
import math


def is_prime(num):
    """
    Checks that given number is a prime number.
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


# py.test
def test_primes():
    # Not primes.
    assert not is_prime(-5)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(125)

    # Primes.
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(31)
    assert is_prime(56509)
    assert is_prime(179425879)
    assert is_prime(32416188583)
