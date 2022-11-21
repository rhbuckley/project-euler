def find_multiples_under(value: int, multiples: list) -> set:
    """
    Find all multiples under a certain value. This function
    will only count multiples once. (i.e. 15 is a multiple of
    both 3 and 5, however, 15 will only be counted once)
    :param value: max value to find multiples under
    :param multiples: list of multiples to search for
    :return: set of all multiples under a value
    """
    # Define multiple list
    multiple_list = set()

    # for every multiple in multiples
    for m in multiples:
        # for each value from m to value with a step of m
        for j in range(m, value, m):
            # add j (each value from m to ...)
            multiple_list.add(j)

    # Return the multiple list
    return multiple_list


if __name__ == "__main__":
    print(sum(find_multiples_under(1000, [3, 5])))
