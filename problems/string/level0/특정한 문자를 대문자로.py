# -*- coding: utf-8 -*-
"""
test
"""


def template(my_string, alp):
    return my_string.replace(alp, alp.upper())


def solution(my_string, alp):
    """문제 해결 함수"""

    print(f"Input: my_string={my_string} alp={alp}")
    print(f"Output: {template(my_string, alp)}")
    return template(my_string, alp)


if __name__ == "__main__":
    my_string, alp = "programmers", "p"
    solution(my_string, alp)
