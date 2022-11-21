from tools.number_tools.is_prime import is_prime


def nth_prime(n: int) -> int:
    """
    Get the nth prime number.
    :param n: nth prime number
    :return: nth prime number
    """
    # Define Prime List
    prime_list = list()

    # Define number accumulator
    num = 1
    # While the length of the prime list != n:
    while sum(prime_list) != n:
        # Append 1 if number is prime, 0 if number is not prime
        prime_list.append(1 if is_prime(num) else 0)
        # append to _num
        num += 1

    index = len(prime_list)
    for j in prime_list[::-1]:
        if j == 1:
            return index
        index -= 1


if __name__ == "__main__":
    print(nth_prime(10_001))