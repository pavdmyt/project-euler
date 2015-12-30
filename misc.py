"""
Some helper functions.
"""
import math


def is_prime(num):
    """
    Checks that given number is a prime number.
    """
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    return False


# py.test
def test_primes():
    # Not primes.
    assert not is_prime(-5)
    assert not is_prime(0)
    assert not is_prime(1)

    # Primes.
    assert is_prime(2)
    assert is_prime(31)
    assert is_prime(56509)
