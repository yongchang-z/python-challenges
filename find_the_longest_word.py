#!/usr/bin/env python3
"""
This function takes a string without punctuation marks as an input and 
return the longest word in the string. If there are multiple words of
the same length, return the first one that appears.
"""


def longest_word(sentence: str) -> str:
    words = sentence.split()

    longest = max(words, default="", key=len)
    return longest


print(longest_word("hello world") == "hello")
print(longest_word("openai gpt-4") == "openai")
print(longest_word("This is a sentence") == "sentence")
print(longest_word("Jumped over the lazy dog") == "Jumped")
print(longest_word("the quick brown fox") == "quick")
print(longest_word("typescript is great") == "typescript")
print(longest_word("the answer is 42") == "answer")
print(longest_word("") == "")
print(longest_word("that is the question") == "question")
