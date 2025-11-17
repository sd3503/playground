# -*- coding: utf-8 -*-


def solution(left, right):
    result = 0
    for i in range(left, right + 1, 1):
        count = sum(1 for x in range(1, i + 1, 1) if i % x == 0)
        if count & 1:
            result -= i
        else:
            result += i

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(43)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint(13, 17)
