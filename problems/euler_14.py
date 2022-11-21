def collatzSequence(starting_num: int) -> list:
    """
    Generates a Collatz Sequence from a particular starting point.
    If the last _num was even, n / 2
    If the last _num was odd, 3n + 1

    Example:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    :param starting_num: number to start with
    :return: list of integers
    """
    # No Cache Solving Method
    n = starting_num
    sequence = list()
    while n > 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else (3 * n) + 1
    return sequence


def cacheExample(starting_num: int, cache):
    # With Cache
    if starting_num == 1:
        return [1]
    elif starting_num % 2 == 0:
        cache[starting_num] = collatzSequence(starting_num // 2, cache)
    else:
        cache[starting_num] = collatzSequence((3 * starting_num) + 1, cache)

    return cache[starting_num]


def largestLenCollatzSequence(max_num: int) -> int:
    # Create a cache
    cache = {}

    max_len, max_input = 0, 0
    # There will always be a number that has a longer sequence
    # than half of the max_num
    for i in range(max_num):
        collatz = collatzSequence(i, cache)

        if len(collatz) > max_len:
            max_len, max_input = len(collatz), i

    print(cache)
    return max_input


if __name__ == "__main__":
    ls = largestLenCollatzSequence(1_000_000)
    print(ls)