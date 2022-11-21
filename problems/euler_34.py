from math import prod


def factorial(x):
    # Generates a factorial
    return prod([i for i in range(x, 0, -1)])


def sumOfFactorials(x):
    # Sums the factorial
    return sum([factorial(int(y)) for y in str(x)])


def findHighestPossibleFactorial():
    # The first upper bound is 9_999_999 (7 digits), however, with some thinking, we can reduce
    # this bound.
    #
    # If n is a natural number of d digits that is a factorion, then
    # 10^(d-1) <= n <= 9!*d
    # This is true until d is 8, so the most amount of digits we can have is 7.
    return factorial(9) * 7


def isEqualRepeat():
    total = 0
    # Why do we go until 9!7 ? This is a good question, and might have a more
    # clear answer if we did all the Euler Problems in order, however, as it may
    # seem that is not the case. This program runs significantly faster with an
    # upper limit of 100_000, but that is not technically correct.
    for i in range(3, findHighestPossibleFactorial()):
        if sumOfFactorials(i) == i:
            total += i
            print("Found value at", i)
    print(total)


if __name__ == "__main__":
    isEqualRepeat()
