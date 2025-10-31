# -*- coding: utf-8 -*-
"""
test
"""


def template(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)


def solution(a, b):
    """문제 해결 함수"""

    print(f"Input: a={a} b={b} ")
    print(f"Output: {template(a, b)}")
    return template(a, b)


if __name__ == "__main__":
    a, b = 2, 91
    solution(a, b)
    a, b = 91, 2
    solution(a, b)
