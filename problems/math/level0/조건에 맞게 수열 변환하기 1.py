# -*- coding: utf-8 -*-


def solution(arr):

    for i, x in enumerate(arr):
        if x >= 50 and not (x & 1):
            arr[i] = x // 2
        elif x < 50 and x & 1:
            arr[i] = x * 2

    return arr


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([2, 2, 6, 50, 99, 49])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([1, 2, 3, 100, 99, 98])
