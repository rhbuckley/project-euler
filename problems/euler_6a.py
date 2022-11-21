def subtract(a, b):
    return a - b


def squared(a):
    return a ** 2


def sum_square_difference(natural_num_len: int) -> int:
    natural_numbers = [x for x in range(1, natural_num_len + 1)]

    # Calculate sum of squares
    sum_squares = sum([squared(i) for i in natural_numbers])
    total_square = sum(natural_numbers) ** 2

    return subtract(total_square, sum_squares)


def main():
    print(sum_square_difference(100))


if __name__ == "__main__":
    main()