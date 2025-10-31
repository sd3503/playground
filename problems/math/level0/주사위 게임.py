# -*- coding: utf-8 -*-
"""
test
"""


def template(a, b, c):
    result = 0

    if a == b == c:
        result = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or b == c or c == a:
        result = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        result = a + b + c
    return result


def solution(a, b, c):
    """문제 해결 함수"""

    print(f"Input: a={a} b={b} c={c}")
    print(f"Output: {template(a, b, c)}")
    return template(a, b, c)


if __name__ == "__main__":
    a, b, c = 2, 6, 1
    solution(a, b, c)
    a, b, c = 5, 3, 3
    solution(a, b, c)
