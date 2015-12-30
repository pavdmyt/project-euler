"""
Problem 6. Sum square difference.
http://static.projecteuler.net/problem=6
"""


def main():
    # Sum of the squares.
    a = sum([i**2 for i in range(101)])

    # Square of the sum.
    b = sum(range(101))**2

    # Result.
    print(b - a)


if __name__ == '__main__':
    main()
