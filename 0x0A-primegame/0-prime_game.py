#!/usr/bin/python3
"""
Module to solve the Prime Game problem where Maria and Ben take turns
removing prime numbers and their multiples from a set of consecutive integers.
"""


def isPrime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def playRound(n):
    """
    Simulate a single round of the game for a given n.

    Args:
        n (int): Upper limit of the game set

    Returns:
        str: Winner of the round ('Maria' or 'Ben')
    """
    # Create a set of available numbers
    numbers = set(range(1, n + 1))

    # Track the current player
    is_maria_turn = True

    while True:
        # Find the largest prime that can be removed
        largest_prime = max((p for p in numbers if isPrime(p)), default=0)

        # If no prime can be removed, current player loses
        if largest_prime == 0:
            return 'Ben' if is_maria_turn else 'Maria'

        # Remove the prime and its multiples
        numbers = set(num for num in numbers if num % largest_prime != 0)

        # Switch turns
        is_maria_turn = not is_maria_turn


def isWinner(x, nums):
    """
    Determine the overall winner across x rounds.

    Args:
        x (int): Number of rounds
        nums (list): List of n values for each round

    Returns:
        str or None: Name of the player who won the most rounds,
                     or None if no winner can be determined
    """
    # Validate inputs
    if not nums or x == 0:
        return None

    # Track wins for each player
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        winner = playRound(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
