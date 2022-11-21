from math import log10, ceil, floor
from functools import reduce

# Numbers from 1 to 19
UNITS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
         'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

# Bases from 10 to 90
B_TEN = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

# Multipliers
BASES = ["HUNDRED", "THOUSAND", "MILLION", "BILLION"]


def get_three_digits(number: int, zeroes: int):
    # get base
    base = BASES[zeroes // 3]

    # if number < 100...
    if number < 100 and zeroes == 0:
        return get_under_100(number)
    elif number < 100 and zeroes != 0:
        return get_under_100(number) + base

    # get first and last digits
    first_digit = get_under_100(number // 100)
    last_digits = get_under_100(number % 100)

    # return result
    if last_digits == '':
        return first_digit + base
    elif base == '':
        return first_digit + last_digits
    elif base == "HUNDRED":
        return first_digit + base + 'AND' + last_digits
    else:
        return first_digit + "HUNDRED" + last_digits + base


def get_under_100(number: int) -> str:
    if number < 20:
        return UNITS[number - 1] if number != 0 else ''
    else:
        if number % 10 == 0: return B_TEN[(number // 10) - 1]
        return B_TEN[(number // 10) - 1] + UNITS[(number % 10) - 1]


def int_to_text(number: int) -> str:
    """ UP TO 999 BILLION """

    # Under Twenty Number
    if number < 20:
        return UNITS[number - 1]

    # The number of digits in an integer is floor(log10(N)) + 1
    num_of_digits = floor(log10(number)) + 1

    # res list
    res_list = []

    i = 0
    while i < num_of_digits:
        nl = []
        for i2 in range(3):
            nl.append(str(number % 10))
            number //= 10
        nl.reverse()
        res_list.append(get_three_digits(int(''.join(nl)), i))
        i += 3

    return "".join(res_list[::-1])


if __name__ == "__main__":
    for i in range(1, 1001): print(int_to_text(i))
    num_letters = sum(map(lambda x: len(int_to_text(x)), range(1, 1001)))
    print(num_letters)
    print('ans', 21124)
