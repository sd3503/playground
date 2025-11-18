# -*- coding: utf-8 -*-


def solution(board, k):
    result = 0
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if i + j <= k:
                result += col

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(8)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]], 2)
