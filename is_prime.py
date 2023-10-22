#!/usr/bin/env python3
import sys


# Brute force algorithm
def is_prime(number):
    """
    Determine if a number is a prime number.
    """
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

# Sieve of eratosthenes algorithm
def sieve(n):
    """
    Accepts an integer as input, output all the prime numbers less than or equal to it.
    """
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1

    primes = [i for i in range(2, n + 1) if prime[i]]

    return primes


def main():
    try:
        number = int(sys.argv[1])
        print(is_prime(number))
        print(sieve(number))
    except:
        print("The argument should be an integer.")


if __name__ == "__main__":
    main()
