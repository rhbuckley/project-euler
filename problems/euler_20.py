# Richard Buckley
# Euler 20
# Factorial Sum

def factorialSum(n: int):
    f = 1
    for i in range(n):
        f *= n - i

    l = [int(x) for x in str(f)]
    return sum(l)


if __name__ == "__main__":
    n1 = factorialSum(100)
    print(n1)
