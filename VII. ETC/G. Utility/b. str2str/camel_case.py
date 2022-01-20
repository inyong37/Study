# Title: Change "(_|-)+" String to Camel Case String with "re" Library.
# Re-Author: Inyong Hwang
# Date: 2022-01-18-Tue
# Description: Change string to camel case string
# Reference: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-96.php

from re import sub


def camel_case(string: str) -> str:
    string = sub(r'(_|-)+', ' ', string).title().replace(' ', '')
    return ''.join([string[0].lower(), string[1:]])
