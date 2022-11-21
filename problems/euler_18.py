import time
from typing import List


def max_path_sum(data, row=0, col=0):
    # We don't need to calculate a sum by adding and checking
    # We just need to find max value

    # If we are on the last row.
    if row == len(data) - 1:
        return data[row][col]

    # Return a sum of max
    return data[row][col] + max(max_path_sum(data, row+1, col+1), max_path_sum(data, row+1, col))


def max_path_sum_mem(data, row=0, col=0, memo=None):
    # If we are on the last row
    if row == len(data) - 1:
        return data[row][col]

    # If we haven't created a memoization yet
    if memo is None:
        memo = {}

    # Have we checked memo yet?
    if (row, col) not in memo:
        memo[(row, col)] = data[row][col] + max(max_path_sum_mem(data, row + 1, col, memo),
                                                max_path_sum_mem(data, row + 1, col + 1, memo))

    # Return memo
    return memo[(row, col)]


def get_int_pyramid(data: str) -> List[List[int]]:
    pyramids = [line.lstrip().split(" ") for line in data.splitlines()]
    int_pyramid = []
    for line in pyramids:
        if line == [""]: continue
        int_pyramid.append(list(map(int, line)))
    return int_pyramid


if __name__ == "__main__":
    f = '''
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

    pyramid = get_int_pyramid(f)

    t0 = time.time()
    sum1 = max_path_sum(pyramid)
    t1 = time.time()
    sum2 = max_path_sum_mem(pyramid)
    t2 = time.time()
    print(f'Recursive answer: {sum1}, calculation time: {t1-t0}')
    print(f'Recursive with memoization answer: {sum2}, calculation time: {t2-t1}')