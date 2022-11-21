def binary_addition(a: tuple, b: tuple) -> tuple:
    """
    Binary addition.

    :param a: the first operand
    :param b: the second operand
    :return: sum
    """
    # Make Sure Both Elements have the same length
    max_len = max(len(a), len(b))
    a = (0,) * (max_len-len(a)) + a
    b = (0,) * (max_len-len(b)) + b

    sum_ = [0] * (max_len + 1)
    carry = 0

    for i in range(max_len - 1, -1, -1):
        # Add the two numbers together
        add = (a[i] + b[i] + carry)
        # Calculate the sum and assign it to the next index
        sum_[i+1] = add - (2 * (add // 2))  # 1 // 2 = 0
        # set carry
        carry = add // 2

    sum_[0] = carry

    if sum_[0] == 0: sum_.remove(0)

    return tuple(sum_)


if __name__ == "__main__":
    a1 = (1, 0, 1)
    b1 = (1, 0, 1)
    x = binary_addition(a1, b1)
    print(x)