from math import sqrt
from typing import Generator


def getFibonacciFormula(n):
    """ this gets the fibonacci value of x by using a formula beret formula """
    return int(round(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)), 0))


def getFibonacciList(until: int) -> Generator[int, None, None]:
    """
    Fibonacci Until
    :param until: ending point (inclusive)
    :return: int
    """

    a, b = 0, 1
    for _ in range(until+1):
        yield a
        a, b = b, a + b


def getFibonacciLoop(until: int) -> int:
    """
    Fibonacci Until
    :param until: ending point (inclusive)
    :return: int
    """

    a, b = 0, 1
    for _ in range(until+1):
        a, b = b, a + b
    return a


# def getFibonacciRecursion(n: int) -> int:
#     """ recursive fibonacci """
#     if n in {0, 1}: return n
#     return getFibonacciRecursion(n - 1) + getFibonacciRecursion(n - 2)


def getFibonacciRecursionCache(n: int) -> int:
    """ a recursive fibonacci sequence with cache """
    # Define Cache
    cache = {0: 0, 1: 1}

    # Define Recursive Function
    def fib_of(n1: int):
        if n1 in cache: return cache[n1]
        cache[n1] = fib_of(n1 - 1) + fib_of(n1 - 2)
        return cache[n1]

    # Run Recursion
    return fib_of(n)


def fastestFibonacci(n: int) -> int:
    """ alias to the fastest sequence """
    '''
    RESULTS: (for i in range(100)
    
    getFibonacciFormula: 120 µs ± 306 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
    getFibonacciLoop: 209 µs ± 6.31 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    list(getFibonacciList): 367 µs ± 5.31 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    getFibonacciRecursionCache: 1.74 ms ± 59.5 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    getFibonacciRecursion: This does not even run with %timeit -n 1 =r 1 Times Out ... Deleted Function
    '''
    return getFibonacciFormula(n)


if __name__ == "__main__":
    for i in range(100):
        print(getFibonacciRecursionCache(i))