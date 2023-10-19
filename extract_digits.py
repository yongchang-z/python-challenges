#!/usr/bin/env python3
"""
Extract the digits of a number
"""
import argparse


def extract_digits(number):
    remaining_value = number
    while remaining_value > 0:
        remaining_value, digit = divmod(remaining_value, 10)
        print(digit, end=" ")
    print()


def main():
    parser = argparse.ArgumentParser(description="Extract digits from a number.")
    parser.add_argument(
        "number", type=int, help="The number from which to extract digits."
    )
    args = parser.parse_args()
    extract_digits(args.number)


if __name__ == "__main__":
    main()
