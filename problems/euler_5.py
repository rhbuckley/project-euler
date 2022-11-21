from tools.number_tools.generate_primes import generate_primes_until
from tools.number_tools.generate_factors import generate_factors_of


def smallest_num_divisible_bf(_from: int, _to: int):
    """
    This is my brute force attempt at solving Euler Problem #5.
    Although this solution does work it is not all that optimal,
    and we can do better.
    :param _from: starting number
    :param _to: ending number (inclusive)
    :return: smallest_num_divisible
    """
    # Define answer variables
    answer = None

    # Define a possible answer
    possible_answer = 1

    while answer is None:
        # For modulo in range from, to (inclusive)
        for mod in range(_from, _to + 1):
            # If the remainder of possible_answer / mod is NOT 0
            if possible_answer % mod != 0:
                # Increment possible_answer
                possible_answer += 1
                # discontinue function
                break
            # If the module is equal to the ending value
            elif mod == _to:
                # set answer to possible_answer
                answer = possible_answer

    # Return Answer (result)
    return answer


def smallest_num_divisible(_from: int, _to: int):
    """
    This is my second attempt at Euler #5. I did use some additional
    material read on internet to fiind that it was not possible to have
    a prime_factor > sqrt(max), so that logic was applied to this equation.
    :param _from: starting number
    :param _to: ending number (inclusive)
    :return: smallest_num_divisible
    """

    # List of possible prime numbers
    primes = generate_primes_until(_to)

    # List of the count of prime numbers
    count = [0] * len(primes)

    # for index in range from, to (inclusive)
    for i in range(_from, _to + 1):
        # prime factors = generate_factors_of(i)
        pf = generate_factors_of(i)

        # for j in the set pf (no repeating prime_factors)
        for j in set(pf):
            # index of = index of j in primes
            io = primes.index(j)
            # add to count of primes. we only want whatever
            # the bigger value is.
            count[io] = max(count[io], pf.count(j))

    # Defiine product accumulator
    total = 1

    # for index, prime number in primes
    for i, prime in enumerate(primes):
        # total *= prime ^ # of primes found
        total *= (prime ** count[i])

    # return total
    return total


if __name__ == "__main__":
    print(smallest_num_divisible(1, 20))  # 232792560
