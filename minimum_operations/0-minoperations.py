#!/usr/bin/python3
"""This module defines the function minOperations"""


def minOperations(n):
    """Calculates the minimum number of operations to obtain exactly n 'H'."""
    if n <= 1:
        return 0

    opCount = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            opCount += divisor
            n //= divisor
        divisor += 1

    return opCount