from tools.binary_tools.shift_left import shift_left
from tools.binary_tools.binary_addition import binary_addition
from tools.binary_tools.tuple_to_base_10 import tuple_to_base_10


def binary_multiplication(a, b):
    """
    Multiply arrays of bits
    :param a: bits
    :param b: bits
    :return: bits
    """
    # Define answer
    ans_ = (0, ) * len(a)

    for i in range(len(b) - 1, -1, -1):
        # If b[i] is not 0 and has a value
        if b[i] != 0:
            ans_ = binary_addition(ans_, a)
        # Shift Left
        a = shift_left(a)
    return ans_


if __name__ == "__main__":
    print(tuple_to_base_10(binary_multiplication((1, 0, 1, 0), (1, 0, 1, 0))))