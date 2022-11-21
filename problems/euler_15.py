import math


def find_paths(k: int, n: int) -> int:
    """
    Finds the number of paths from (0, 0) to
    (k, n). The formula for counting the number
    of combinations of k out of n objects
    ("k choose n") is:

    nCk = n! / ( (n-k)!*k! )

    :param k:
    :param n:
    :return:
    """
    # n is not a coordinate, it is n choose k
    n = n + k
    return math.factorial(n) // (math.factorial(n-k) * math.factorial(k))


def lattice_paths(height: int, width: int) -> int:
    """
    How many paths are there from the top left
    corner to the bottom right corner? ** We can
    only move to the right and down.
    :param height: int
    :param width: int
    :return: # of paths
    """
    return find_paths(height, width)


"""
Helpful Resource: 
https://stemhash.com/counting-lattice-paths/
We used combinatrics to figure this problem out. 
!! k choose n formula is very important

1. Add the two coordinates together as n
2. k choose n
"""

if __name__ == "__main__":
    print(lattice_paths(12, 8))