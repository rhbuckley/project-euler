# Richard Buckley
# Euler 21
from rhbuck_tools.number_tools.generate_factors import generate_factors_of


def amicableNumbers(until: int):
    amicableNums = set()
    for num in range(until):
        a = sum(generate_factors_of(num, trimSelf=True, sort=False))
        b = sum(generate_factors_of(a, trimSelf=True, sort=False))

        if b == num and a != b:
            amicableNums.add(b)

    return sum(amicableNums)


if __name__ == "__main__":
    print(amicableNumbers(10000))
