def perfect_squares(until: int):
    """
    Get a list of perfect squares until a number.
    :param until: number
    :return: list of perfect squares
    """
    # pfsquares_list
    pfsquares_list = []

    # Define counter
    u = 1

    # While u^2 is less than until
    while u ** 2 < until:
        # add u^2 to list
        pfsquares_list.append(u**2)
        # increment u
        u += 1

    # return the result
    return pfsquares_list


if __name__ == "__main__":
    print(perfect_squares(100))