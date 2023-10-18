#!/usr/bin/env python3
"""
This function take three strings as input: the main text, the target substring, and the 
replacement substring. It returns a new string where all occurrences of the target substring
within the main text are replaced with the replacement substring.
"""


def replace_all(mainText: str, target: str, repl: str) -> str:
    import re

    return re.sub(re.escape(target), repl, mainText)


print(replace_all("hello world", "world", "TypeScript") == "hello TypeScript")
print(
    replace_all("hello world world", "world", "TypeScript")
    == "hello TypeScript TypeScript"
)
print(replace_all("TypeScript is fun", "fun", "awesome") == "TypeScript is awesome")
print(replace_all("aaa", "a", "b") == "bbb")
print(replace_all("replace all the all", "all", "some") == "replace some the some")
print(replace_all("123 123", "123", "321") == "321 321")
print(replace_all("OpenAI", "AI", "Source") == "OpenSource")
print(replace_all("", "anything", "nothing") == "")
