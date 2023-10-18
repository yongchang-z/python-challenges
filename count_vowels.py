#!/usr/bin/env python3
"""
This function takes a string as an input and return the count of vowels in the string.
The function is case-insensitive.
"""


def count_vowels(text: str) -> int:
    # vowels = set("aeiouAEIOU")
    # counts = 0
    # for char in text:
    #     if char in vowels:
    #         counts += 1
    # return counts

    vowels = "aeiouAEIOU"
    return sum(text.count(vowel) for vowel in vowels)


print(count_vowels("hello") == 2)
print(count_vowels("openai") == 4)
print(count_vowels("typescript") == 2)
print(count_vowels("a") == 1)
print(count_vowels("b") == 0)
print(count_vowels("AEIOU") == 5)
print(count_vowels("") == 0)
