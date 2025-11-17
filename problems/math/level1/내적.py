# -*- coding: utf-8 -*-


def solution(a, b):
    result = 0
    for aa, bb in zip(a, b):
        result += aa * bb

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(3)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint([1, 2, 3, 4], [-3, -1, 0, 2])
