#!/usr/bin/env python3
"""
Accepts a string input, and return the length of the longest subring without repeating characters.
"""

def longest_substring(s: str) -> int:
    start = result = 0
    chars = {}

    for index, char in enumerate(s):
        if char in chars:
            start = max(start, chars[char] + 1)
        chars[char] = index
        result = max(result, index - start + 1)
    
    return result


print(longest_substring("abcabcbb") == 3)
print(longest_substring("bbbbb") == 1)
print(longest_substring("pwwwkew") == 3)
print(longest_substring("abcdef") == 6)
print(longest_substring("") == 0)
print(longest_substring("au") == 2)