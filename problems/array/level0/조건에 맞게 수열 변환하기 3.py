# -*- coding: utf-8 -*-
"""
test
"""


def template(arr, k):
    result = []
    if k & 1:
        result = [x * k for x in arr]
    else:
        result = [x + k for x in arr]

    return result


def solution(arr, k):

    print(f"Input: arr={arr} k={k}")
    print(f"Output: {template(arr, k)}")
    return template(arr, k)


if __name__ == "__main__":
    arr, k = [1, 2, 3, 100, 99, 98], 3
    solution(arr, k)
    arr, k = [1, 2, 3, 100, 99, 98], 2
    solution(arr, k)
