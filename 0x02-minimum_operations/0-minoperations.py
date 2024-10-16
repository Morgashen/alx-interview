#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations
needed to result in exactly n 'H' characters in a file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters.

    Args:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations. Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    # Example usage
    n = 9
    print(f"Min operations for n = {n}: {minOperations(n)}")
