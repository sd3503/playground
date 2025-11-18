# -*- coding: utf-8 -*-


def solution(a, d, included):
    result = 0
    for i, x in enumerate(included):
        if x:
            result += i * d + a

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(37)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(3, 4, [True, False, False, True, True])
