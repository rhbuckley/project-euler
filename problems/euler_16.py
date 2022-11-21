from rhbuck_tools.binary_tools.binary_multiplication import binary_multiplication
from rhbuck_tools.binary_tools.tuple_to_base_10 import tuple_to_base_10
from datetime import datetime


def power_digit_sum(power: int) -> int:
    """
    Sum the digits of the number _num^power

    We are going to solve this in _bin to make
    it a bit more exciting. So the number will
    equal 2.
    :param power: int
    :return: sum
    """
    stored_bin = (1, 0)
    for i in range(power - 1):  # we already have 2^0 in stored_bin
        stored_bin = binary_multiplication(stored_bin, (1, 0))

    # Here's the value
    val = str(tuple_to_base_10(stored_bin))

    # Sum each digit in this...
    sum_ = 0
    for char in val:
        sum_ += int(char)

    return sum_


def power_digit_sum_easy(power:int) -> int:
    """
    Easier Solution
    :param power:
    :return:
    """
    val = 2
    for i in range(power - 1):
        val *= 2

    val = str(val)

    sum_ = 0
    for char in val:
        sum_ += int(char)

    return sum_

"""
Even though the _bin stuff was fun, it took longer than the easy solution. Why?
Well, there may have been too much list manipulation. ( I think there was ), especially
with reversing the lists for _bin operations.
"""
if __name__ == "__main__":
    print("Binary Solution")
    dt_start = datetime.now()
    x = power_digit_sum(1000)
    print(x)
    print("that took", str(datetime.now() - dt_start))

    print("Easy Solution")
    dt_start = datetime.now()
    x = power_digit_sum_easy(1000)
    print(x)
    print("that took", str(datetime.now() - dt_start))
