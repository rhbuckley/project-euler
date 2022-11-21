from typing import Union


def is_palindrome(value: Union[str, int]) -> bool:
    """
    Checks to see whether a particular value (int or string) is a palindrome.
    A palindrome is a value where the value is mirrored when being split down the middle.
    For example, tacocat and 1001 are palindromes.

    This function ignores case.
    :param value: <str | int> the value to check
    :return: <bool> is the function a palindrome
    """
    # If value is in convert to string
    value = str(value).upper()

    # See if the string is the same thing as the string reversed
    return value == value[::-1]
