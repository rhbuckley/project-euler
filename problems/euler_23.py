# Richard Buckley
# Euler 23
from tools.number_tools.generate_factors import generate_factors_of

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''


def main(_max: int):
    abundant = []
    for i in range(_max + 1):
        # Get Proper Divisors
        divisors = generate_factors_of(i, trimSelf=True)
        factorSum = sum(divisors)
        if factorSum > i: abundant.append(i)

    isRepresented = [0] * (_max + 1)
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] > _max: break
            isRepresented[abundant[i] + abundant[j]] = 1

    answer = 0
    for i in range(len(isRepresented)):
        if not isRepresented[i]:
            answer += i
    return answer


if __name__ == "__main__":
    print(main(28123))

