from rhbuck_tools.number_tools.generate_factors import generate_factors_of


def triangle_numbers() -> [list, list]:
    """
    Returns a list of triangle numbers until a certain value. A triangle number is
    the sum of all natural numbers that occured before it.

    EXAMPLE (triangle number: factors):
         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
    :return: [triangle_numbers, triangle_numbers_factors]
    """
    # (n)(n + 1) / 2
    t_numbers = [1]
    t_factors = [[1]]

    n = 2
    # while t_numbers[-1] < until:
    while len(t_factors[-1]) < 500:
        _tnum = int((n * (n + 1)) / 2)  # ( n(n+1) ) / 2
        _tfac = generate_factors_of(_tnum)

        t_numbers.append(_tnum)
        t_factors.append(_tfac)

        n += 1

    return t_numbers, t_factors


if __name__ == "__main__":
    tnum, tfac = triangle_numbers()
    print(tnum[-1])