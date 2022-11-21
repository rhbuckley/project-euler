def sum_square_difference(natural_num_len: int) -> int:
    """
    This is my attempt at euler 6. The problem will return the
    difference of eacn number from one to x squared and the sum
    of all numbers from one to x squared.

    ex. 1*^2 2^2 = (1 + 2)^2
    :param natural_num_len: length of natural numbers
    :return: answer of problem
    """
    # List of all natural numbers from 0 to len of natural numbers
    natural_numbers = [x for x in range(1, natural_num_len + 1)]

    # Calculate sum of squares
    sum_squares = sum([i**2 for i in natural_numbers])
    total_square = sum(natural_numbers) ** 2

    return total_square - sum_squares


def main():
    print(sum_square_difference(100))


if __name__ == "__main__":
    main()