"""
Problem 9. Special Pythagorean triplet.
http://static.projecteuler.net/problem=9
"""
import math


def gen_divisor_pairs(num):
    """
    Generates factor-pairs of the given number.
    E.g. factor-pairs of 18 are: (1, 18), (2, 9), (3, 6)
    """
    for divisor in range(1, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            yield divisor, num / divisor


def gen_triples():
    """
    Generates Pythagorean triples using Dickson's method.

    To find triples: a^2 + b^2 = c^2,
    find ints r, s and t such that: r^2 = 2*s*t
    Then:
      a = r + s, b = r + t, c = r + s + t
    """
    r = 2  # any even int.
    while True:
        st = r**2 / 2
        pairs = [pair for pair in gen_divisor_pairs(st)]
        for pair in pairs:
            s, t = pair
            yield r + s, r + t, r + s + t
        r += 2


def main():
    for triple in gen_triples():
        if sum(triple) == 1000:
            a, b, c = triple
            print(a * b * c)
            break


if __name__ == '__main__':
    main()
