# -*- coding: utf-8 -*-


def solution(arr):

    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            if arr[i][j] != arr[j][i]:
                return 0

    return 1


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(1)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(
        [
            [19, 498, 258, 587],
            [63, 93, 7, 754],
            [258, 7, 1000, 723],
            [587, 754, 723, 81],
        ]
    )
