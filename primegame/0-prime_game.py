#!/usr/bin/python3
"""
Prime Game
"""


def sieve_of_eratosthenes(max_n):
    """Use Sieve of Eratosthenes to find all primes up to max_n."""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False
    return primes


def count_prime_moves(n, primes):
    """Count how many prime moves can be made in a game with n."""
    moves = 0
    nums = [True] * (n + 1)  # True means the number is still available
    for i in range(2, n + 1):
        if primes[i] and nums[i]:  # if the number is a prime and still available
            moves += 1
            for multiple in range(i, n + 1, i):
                # Mark prime and its multiples as removed
                nums[multiple] = False
    return moves


def isWinner(x, nums):
    """Determine the winner of each round."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)  # Find the maximum number in the input list
    primes = sieve_of_eratosthenes(max_n)  # Precompute primes up to max_n

    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        moves = count_prime_moves(n, primes)
        # Maria starts first, so if moves are odd, Maria wins, otherwise Ben
        # wins
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
