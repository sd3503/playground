# -*- coding: utf-8 -*-


def solution(numbers):

    reslut = 0
    for x in range(0, 10, 1):
        if x not in numbers:
            reslut += x

    return reslut


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(14)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint([1, 2, 3, 4, 6, 7, 8, 0])
    solution([1, 2, 3, 4, 6, 7, 8, 0])
