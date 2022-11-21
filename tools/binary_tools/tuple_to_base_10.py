from typing import Union, Tuple, List


def tuple_to_base_10(t: Union[Tuple, List]) -> int:
    """
    Convert a tuple to base 10
    :param t: Tuple or List
    :return:
    """
    # Define a sum
    sum_ = 0

    # Convert Tuple to List
    t = list(t)

    # Reverse t
    t.reverse()

    # Enumerate List and Iterate
    for i, val in enumerate(t):
        # Validate Inputs
        if val not in [0, 1]: raise ValueError
        # Append to sum
        sum_ += (2**i) * val

    # Return a sum
    return sum_


if __name__ == "__main__":
    test_val = "10111011100"
    test_list = [int(char) for char in test_val]
    print(tuple_to_base_10(test_list))
    print(tuple_to_base_10((0, 1, 1, 1, 0)))