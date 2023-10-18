#!/usr/bin/env python3
"""
count the occurrences of a substring within a given main string, case-insensitive.
"""

import re

# 
# def count_occurrences(main_str: str, sub_str: str) -> int:
    # matches = re.findall(rf"(?={sub_str})", main_str, flags=re.IGNORECASE)
    # return len(matches)

# Without using re
def count_occurrences(main_str: str, sub_str: str) -> int:
   ind = res = 0
   while (ind := main_str.lower().find(sub_str.lower(), ind)) != -1:
       res += 1
       ind += 1
   return res

print(count_occurrences("Hello World hello", "hello") == 2)
print(count_occurrences("hello", "world") == 0)
print(count_occurrences("hello world hello", "hello") == 2)
print(count_occurrences("hello world hello world hello", "world") == 2)
print(count_occurrences("HELLO", "hello") == 1)
print(count_occurrences("HELLO WORLD", "WORLD") == 1)
print(count_occurrences("hello world hello", "o w") == 1)
print(count_occurrences("apple apple apple", "apple") == 3)
print(count_occurrences("apple Apple apple", "apple") == 3)
print(count_occurrences("apple", "APPLE") == 1)
