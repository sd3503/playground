# -*- coding: utf-8 -*-


def solution(arr, flag):
    result = []
    for f, a in zip(flag, arr):
        if f:
            for j in range(a * 2):
                result.append(a)
        else:
            for j in range(a):
                result.pop()

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([3, 3, 3, 3, 4, 4, 4, 4])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([3, 2, 4, 1, 3], [True, False, True, False, False])
