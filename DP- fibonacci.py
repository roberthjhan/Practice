"""
A very basic example of dynamic programming. Here we
save the previously calculated fibonacci values to a
list. These values or rather the last two values are
used to calculate the next number in the sequence.

"""


def fib(N: int) -> int:
    fibonacci = [0, 1]
    if N == 0: # Need to return first value rather than last
        return 0
    while len(fibonacci) < N + 1:
        # Calculate next number in sequence using last two calculations
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[-1]