"""
Problem 7. 10001st prime.
http://static.projecteuler.net/problem=7
"""
import misc


def main():
    counter = 1
    num = 1
    while counter < 10001:
        num += 2
        if misc.is_prime(num):
            counter += 1
    print(num)


if __name__ == '__main__':
    main()
