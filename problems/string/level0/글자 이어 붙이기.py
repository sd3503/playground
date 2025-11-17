# -*- coding: utf-8 -*-
"""
test
"""


def template(my_string, index_list):

    result = "".join(my_string[i] for i in index_list)

    return result


def solution(my_string, index_list):
    """문제 해결 함수"""

    print(f"Input: my_string={my_string}, index_list={index_list}")
    print(f"Output: {template(my_string, index_list)}")
    return template(my_string, index_list)


if __name__ == "__main__":
    my_string, index_list = "cvsgiorszzzmrpaqpe", [
        16,
        6,
        5,
        3,
        12,
        14,
        11,
        11,
        17,
        12,
        7,
    ]
    solution(my_string, index_list)
