"""
Problem 10. Summation of primes.
http://static.projecteuler.net/problem=10
"""
import misc


def main():
    res = 2
    for num in range(3, 2000000, 2):
        if misc.is_prime(num):
            res += num
    print(res)


if __name__ == '__main__':
    main()
