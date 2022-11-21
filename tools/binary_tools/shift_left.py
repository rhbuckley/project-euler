from typing import Union, List, Tuple


def shift_left(t: Union[List, Tuple], n: int = 1) -> Union[List, Tuple]:
    """
    Shifts a list of bits to the left by adding n 0s on the right.
    :param t: List or Tuple
    :param n: Number of places t shift by
    :return: List or Tuple
    """
    # Check to see what type input was
    is_list = type(t) is list

    # Shift List as tuple
    shifted_tuple = tuple(t) + (0,) * n

    # Convert to List if original was list
    return list(shifted_tuple) if is_list else shifted_tuple






