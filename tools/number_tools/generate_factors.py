from functools import reduce
from tools.number_tools.is_prime import is_prime


def generate_factors_of(num: int, sort: bool = True, trimSelf: bool = False) -> list:
    """
    Generate a list of factors of a certain number. This function
    will completely factor a number. For example, 20 will return
    2, 2, 5.
    :param num: <int> the number to generate primes of
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


def generate_prime_factors_of(num: int) -> list:
    """
    Generate a list of factors of a certain number
    :param num: <int> the number to generate primes of
    :return: <list> a list of prime numbers
    """
    factors = generate_factors_of(num)
    return [x for x in factors if is_prime(x)]


if __name__ == "__main__":
    print(generate_factors_of(1000))
    print(generate_factors_of(20))