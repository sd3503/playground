# -*- coding: utf-8 -*-
"""
test
"""

import re


def template(myString):
    result = re.sub(r"[a-l]", "l", myString)
    return result


def solution(myString):
    print(f"Input: myString={myString} \n  Output: {template(myString)}")
    return template(myString)


if __name__ == "__main__":
    myString = "abcdevwxyz"
    solution(myString)
