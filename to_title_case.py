#!/usr/bin/env python3
"""
This function takes a string as input and convert all the first letters of the words to uppercase,
making the string a title case.
"""


def to_title_case(sentence: str) -> str:
    import re

    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(), sentence
    )


print(to_title_case("hello world") == "Hello World")
print(to_title_case("openai gpt-4") == "Openai Gpt-4")
print(to_title_case("this is a title") == "This Is A Title")
print(to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox")
print(to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog")
print(to_title_case("typescript is great") == "Typescript Is Great")
print(to_title_case("the answer is 42") == "The Answer Is 42")
print(to_title_case("") == "")
print(to_title_case("anna's dog") == "Anna's Dog")
