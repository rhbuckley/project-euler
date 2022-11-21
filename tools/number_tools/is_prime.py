from math import sqrt


def is_prime(n: int) -> bool:
    """
    Checks to see whether a number is prime
    :param n: number to check if is prime
    :return: boolean
    """

    # Handle n being 1
    if n == 1:
        return False

    # We could use brute forcing to check if a number is prime or not
    # but that isn't all that efficient. After doing some research, I
    # found that it was possible to loop from 2 to int(sqrt(n))
    for i in range(2, int(sqrt(n)) + 1):
        # Is n CLEANLY divisible by x ? (i.e. no remainder)
        if n % i == 0:
            # n has a factor between 2 and sqrt(n)...
            # n is not a prime number
            return False

    # no prime factors found? then the number is in fact prime
    return True
