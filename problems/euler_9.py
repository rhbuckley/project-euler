from math import sqrt, prod
from rhbuck_tools.number_tools.perfect_squares import perfect_squares


def pythagorean_triplet(equals):
    """
    This is my attempt at euler #9. In this problem,
    we are trying to find the values of a, b and c where
    a + b + c = 1000 where a^2 + b^2 = c^2. Since these
    are NATURAL NUMBERS, we can get a list of perfect
    squares and then determine which squares add to 1000.
    :param equals: a + b + c equals ??
    :return: list [a, b, c]
    """
    # Define a list of perfect squares
    # we are getting perfect squares until equals^2 because
    # will end up sqrting equals
    num_squared = [int(sqrt(i)) for i in perfect_squares(equals ** 2)]
    pfsquares = perfect_squares(equals ** 2)
    #
    # for unsquared numbers and squared numbers
    for (unsquared1, squared1) in zip(num_squared, pfsquares):
        # for unsquared numbers and squared numbers
        for (unsquared2, squared2) in zip(num_squared, pfsquares):
            # c = sqrt(unsquared1 + squared2)
            c = sqrt(squared1 + squared2)
            # if c is not an integer, continue
            if not c.is_integer(): continue
            # if a + b + c == 1000
            if unsquared1 + unsquared2 + c == 1000:
                # return answer
                return [unsquared1, unsquared2, int(c)]


if __name__ == "__main__":
    print(pythagorean_triplet(1000))
    print(prod(pythagorean_triplet(1000)))
