from math import sqrt


def generate_primes_until(max_num: int) -> list:
    """
    Generate a list of prime numbers until a certain number
    :param max_num: <int> The largest possible prime number to get
    :return: <list> a list of prime numbers
    """
    # Calculating a list of prime numbers is generally very resource
    # intensive so in hopes of making the most efficeint code, we will
    # be using the Sieve of Eratosthenes
    # basically, we don't look for primes, we look for compsite numbers

    # Fix max num to include itself.
    max_num += 1

    # Define the list of whether the numbers we have are prime
    # or not... 0 = composite, 1 = prime. We assume that the
    # number is prime, but will get back to this later
    n_list = [1] * max_num

    # Like in the is_prime function, we know that prime number can only
    # occur from 2 to sqrt(n)
    for i in range(2, int(sqrt(max_num))):
        if n_list[i] == 0:
            continue

        # For all the multiples of i
        for j in range(2*i, max_num, i):
            # We need to go from twice of i with
            # a step of i to the max_num
            n_list[j] = 0

    # Return a list of prime numbers... we add every element
    # that is prime from a range of max_num
    return [i for i in range(2, max_num) if n_list[i] == 1]


if __name__ == "__main__":
    print(generate_primes_until(20))