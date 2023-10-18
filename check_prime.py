#!/usr/bin/env python3
"""
This function prints all the prime numbers less than the input number.
"""

def check_prime1(num):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for n in range(2, num):
        if is_prime(n):
            print('A:', n, 'is a prime number')


# A more straight forward but less efficient method:
def check_prime2(num):
    for n in range(2, num):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print('B:', n, 'is a prime number')

      
check_prime1(1000)
check_prime2(1000)