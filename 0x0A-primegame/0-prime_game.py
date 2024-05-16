#!/usr/bin/python3
"""
Defines isWinner function that's a solution to the Prime number Game """


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. Lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime number Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        name of the player that won the most rounds
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
