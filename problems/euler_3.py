from tools.number_tools.generate_factors import generate_prime_factors_of


def largest_primes(max_num: int):
    # Get list of prime numbers
    prime_list = generate_prime_factors_of(max_num)

    # Return max value in list
    return max(prime_list)


if __name__ == "__main__":
    print(largest_primes(600851475143))