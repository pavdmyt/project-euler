"""
Problem 2. Even Fibonacci numbers.
http://static.projecteuler.net/problem=2
"""


LIMIT = 4 * 10**6


def genfib(maxval):
    a, b = 1, 1
    while b < maxval:
        yield b
        a, b = b, a + b


def main():
    even_fib_nums = [num for num in genfib(LIMIT) if num % 2 == 0]
    res = sum(even_fib_nums)
    print(res)


if __name__ == '__main__':
    main()
