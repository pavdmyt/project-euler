"""
Problem 10. Summation of primes.
http://static.projecteuler.net/problem=10
"""
import misc


def main():
    res = misc.sieve_Erat(2000000)
    print(sum(res))


if __name__ == '__main__':
    main()
