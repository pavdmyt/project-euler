"""
Problem 4. Largest palindrome product.
http://static.projecteuler.net/problem=4
"""


def reverse_num(num):
    """
    Reverse given number.
    123 -> 321
    """
    lst = [digit for digit in str(num)]
    return int(''.join(lst[::-1]))


def is_palindrome(num):
    """
    Checks if number is a palindrome.
    """
    return num == reverse_num(num)


def main():
    rng = range(100, 1000)
    products_set = {i*j for i in rng for j in rng}
    palindromes = filter(is_palindrome, products_set)
    print(max(palindromes))


if __name__ == '__main__':
    main()
