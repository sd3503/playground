# -*- coding: utf-8 -*-

import math


def solution(n):
    result = [[0] * n for _ in range(n)]  # 각각 독립적인 리스트 생성
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    acts = []

    for i in range((n - 2) * 2 + 3):
        temp = 0
        if i <= 2:
            temp = n - 1
        else:
            temp = n - 1 - (i - 1) // 2
        for j in range(temp):
            if i % 4 == 0:
                acts.append(move[0])
            if i % 4 == 1:
                acts.append(move[1])
            if i % 4 == 2:
                acts.append(move[2])
            if i % 4 == 3:
                acts.append(move[3])
    x = 0
    y = 0
    for i, act in enumerate(acts):
        result[y][x] = i + 1

        y += act[0]
        x += act[1]
    result[y][x] = n**2
    return result


def customPrint(*args):

    req_out = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]

    get_out = solution(*args)
    # print("Input:", args)
    print("req_output:", req_out)
    print("get_output:", get_out)
    print(
        "------------------------success------------------------"
        if req_out == get_out
        else "------------------------fail------------------------"
    )


if __name__ == "__main__":
    customPrint(5)
