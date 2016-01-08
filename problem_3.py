"""
Problem 3. Largest prime factor.
https://projecteuler.net/problem=3
"""
import math


NUM = 600851475143
near_sqrt = int(math.sqrt(NUM))


def primes_below_num(num):
    """
    Returns a list of all primes below given number.
    """
    res = range(2, num+1)
    for i in range(2, int(math.sqrt(num))):
        res = filter(lambda x: x == i or x % i, res)
    return res


def main():
    # There is no reason to search prime factors greater
    # than square root of the given number.
    primes_lst = primes_below_num(near_sqrt)
    factors_lst = [prime for prime in primes_lst if NUM % prime == 0]
    res = max(factors_lst)
    print(res)


if __name__ == '__main__':
    main()
