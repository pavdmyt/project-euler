"""
Problem 5. Smallest multiple.
http://static.projecteuler.net/problem=5
"""


def is_divisible(num):
    """
    Checks if number is evenly divisible by all
    of the numbers from 1 to 20.
    """
    for i in [3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
        if num % i != 0:
            return False
    return True


def main():
    num = 2520
    while True:
        if is_divisible(num):
            print(num)
            break
        num += 20


if __name__ == '__main__':
    main()
