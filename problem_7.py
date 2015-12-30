"""
Problem 7. 10001st prime.
http://static.projecteuler.net/problem=7
"""
import misc


def main():
    lst = [2]
    num = 3
    while len(lst) < 10001:
        if misc.is_prime(num):
            lst.append(num)
        num += 2
    print(lst[-1])


if __name__ == '__main__':
    main()
