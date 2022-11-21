import itertools
from functools import reduce

from tools.number_tools.is_prime import is_prime
from tools.other.flatten import flatten
from itertools import chain, combinations
from math import ceil, sqrt
from operator import mul


def generate_factors_of(num: int, sort: bool = True, trimSelf: bool = False) -> list:
    """
    Generate a list of factors of a certain number. This function
    will completely factor a number. For example, 20 will return
    2, 2, 5.
    :param num: <int> the number to generate factors of
    :param sort: <boolean> should output be sorted?
    :param trimSelf <boolean> sometimes we don't want itself as a factor
    :return: <list> a list of factors
    """
    factors = set()

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)

    if trimSelf and num in factors: factors.remove(num)
    if sort: return sorted(factors)
    return list(factors)


# def generate_factors_of_memo(num: int, memo: dict, sort: bool = True, trimSelf: bool = False) -> [list, dict]:
#     """
#     Generate a list of factors of a certain number. This function
#     will completely factor a number. For example, 20 will return
#     2, 2, 5. This is a BAD solution because it requires the use of a dict
#     which can simplify SOME of the process, but it will still end up taking
#     a longer amount of time
#     :param num: <int> the number to generate factors of
#     :param memo: <dict> the number that we have generated factors of
#     :param sort: <boolean> should output be sorted?
#     :param trimSelf <boolean> sometimes we don't want itself as a factor
#     :return: <list> a list of factors
#     """
#     factors = set()
#
#     # Handle Empty Memo
#     if len(memo) == 0: memo = {0: {0}, 1: {1}}
#
#     for i in range(1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             if num // i in memo:
#                 for n in memo[num // i]:
#                     x = n * i
#                     factors.add(x)
#                     factors.add(num // x)
#             else:
#                 factors.add(i)
#                 factors.add(num // i)
#     memo[num] = set(factors)
#
#     if trimSelf and num in factors: factors.remove(num)
#     if sort: return sorted(factors), memo
#     return list(factors), memo


def generate_factors_with_primes(num: int, sort: bool = True, trimSelf: bool = False):
    """
    This is a more creative approach, but let's see if this works
    :param num:
    :param sort:
    :param trimSelf:
    :return:
    """

    def breakDown(x):
        if is_prime(x): return x
        for i in range(ceil(sqrt(x)), 1, -1):
            if x % i == 0:
                return flatten([breakDown(x // i), breakDown(i)])

    basics = breakDown(num)
    factors = set(chain(*(combinations(basics, i) for i in range(1, len(basics) + 1))))
    res = set([reduce(mul, f, 1) for f in factors] + ([1] if trimSelf else [1, num]))

    return sorted(res) if sort else list(res)


def generate_prime_factors_of(num: int) -> list:
    """
    Generate a list of factors of a certain number
    :param num: <int> the number to generate primes of
    :return: <list> a list of prime numbers
    """
    factors = generate_factors_of(num)
    return [x for x in factors if is_prime(x)]


if __name__ == "__main__":
    print(generate_factors_with_primes(204))
    print(generate_factors_of(204))
