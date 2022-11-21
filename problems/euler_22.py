import numpy as np


def main():
    unsorted_list = np.loadtxt("./resources/euler_22/p022_names.txt", dtype=str, delimiter=",", quotechar='"')

    # lmao u thought I was going to learn a good sorting algorithm
    sorted_list = np.sort(unsorted_list)

    getCharVal = lambda x: sum([ord(c.lower()) - 96 for c in x])

    total_name_sum = 0
    for i, name in enumerate(sorted_list):
        j = i + 1  # bump
        total_name_sum += getCharVal(name) * j

    print(total_name_sum)


if __name__ == "__main__":
    main()
