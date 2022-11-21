from math import log10, ceil
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''


def fibonacci(n):
    a, b = 0, 1
    i = 0
    while a == 0 or ceil(log10(a)) < n:
        a, b = b, a + b
        i += 1
    return i  # a for number


if __name__ == "__main__":
    print(fibonacci(1000))
