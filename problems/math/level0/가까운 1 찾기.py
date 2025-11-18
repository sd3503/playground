# -*- coding: utf-8 -*-


def solution(arr, idx):
    for i in range(idx, len(arr), 1):
        if arr[i] == 1:
            return i

    return -1


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(3)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([1, 0, 0, 1, 0, 0], 4)
