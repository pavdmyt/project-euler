"""
Some helper functions.
"""
import math


def is_prime(num):
    """
    Checks that given number is a prime number.
    """
    if num <= 3:
        return num == 2 or num == 3

    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def sieve_Erat(num):
    """
    Returns all primes below given number.
    Sieve of Eratosthenes is used.
    """
    sieve = [True] * (num + 1)
    for i in range(2, int(math.sqrt(num)) + 1):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    return [i for i in range(2, num + 1) if sieve[i]]


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


def test_sieve_Erat():
    def case(num):
        ref_lst = [i for i in range(num + 1) if is_prime(i)]
        assert sieve_Erat(num) == ref_lst

    for num in [0, 1, 2, 3, 100, 2001, 15023]:
        case(num)
