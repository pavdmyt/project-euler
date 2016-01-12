"""
Problem 4. Largest palindrome product.
http://static.projecteuler.net/problem=4
"""


def main():
    rng = range(100, 1000)
    products_set = {i*j for i in rng for j in rng}
    is_palindrome = lambda num: str(num) == str(num)[::-1]
    palindromes = filter(is_palindrome, products_set)
    print(max(palindromes))


if __name__ == '__main__':
    main()
