"""
Problem 3. Largest prime factor.
https://projecteuler.net/problem=3
"""
import math


NUM = 600851475143


def prime_factors(num):
    """
    Returns a list of primes factors for the given number.
    """
    factors = []
    # Handle 2
    while num % 2 == 0:
        factors.append(2)
        num /= 2

    # Handle all odd nums <= sqrt(num)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num /= i

    # Handle num is prime
    if num > 2:
        factors.append(num)

    return factors


def main():
    factors = prime_factors(NUM)
    print(max(factors))


if __name__ == '__main__':
    main()
