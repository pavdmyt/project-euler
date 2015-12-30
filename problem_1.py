"""
Problem 1. Multiples of 3 and 5.
https://projecteuler.net/problem=1
"""


def main():
    ismul = lambda x: x % 3 == 0 or x % 5 == 0
    lst = [num for num in range(1000) if ismul(num)]
    res = sum(lst)
    print(res)


if __name__ == '__main__':
    main()
