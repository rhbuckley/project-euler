from rhbuck_tools.number_tools.generate_primes import generate_primes_until


def summation_of_primes(below: int) -> int:
    """
    This is my attempt at Euler 10, the summation of primes. I
    think that this should go by pretty quickly, as I have already
    written some functions that should help with this problem.

    Actually I just finished (within a minute) thank god for these reusable
    functions.

    :param below: int
    :return: sum of primes
    """
    primes = generate_primes_until(below)
    return sum(primes)


if __name__ == "__main__":
    print(summation_of_primes(2_000_000))
