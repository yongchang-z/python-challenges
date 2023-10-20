#!/usr/bin/env python3
"""
Determine all real divisors of a number.
"""

import sys

# def find_proper_divisors(number):
#     divisors = [1]
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             divisors.append(i)
#     return divisors

# List comprehension approach
def find_proper_divisors(number):
    proper_divisors = [i for i in range(2, number // 2 + 1) if number % i == 0]
    return proper_divisors

def main():
    if len(sys.argv) != 2:
        print("One and only one argument expected.")
        raise SystemExit(2)
    try:
        number = int(sys.argv[1])
        print(find_proper_divisors(number))
    except:
        print("The argument should be an integer.")

if __name__ == "__main__":
    main()