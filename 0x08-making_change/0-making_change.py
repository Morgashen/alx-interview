#!/usr/bin/python3
"""
Module for solving the coin change problem.
Determines the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations available
        total (int): Target amount to make change for

    Returns:
        int: Fewest number of coins needed, or -1 if impossible
    """
    # If total is 0 or negative, return 0
    if total <= 0:
        return 0

    # Initialize dp array with a large value (impossible to exceed)
    # We use total + 1 as the "impossible" marker
    dp = [total + 1] * (total + 1)

    # 0 amount requires 0 coins
    dp[0] = 0

    # Iterate through all possible amounts from 1 to total
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # If the coin value is less than or equal to current amount
            if coin <= amount:
                # Update minimum coins needed for this amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still the initial "impossible" value, return -1
    return dp[total] if dp[total] != total + 1 else -1
