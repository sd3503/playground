# -*- coding: utf-8 -*-


def solution(number):

    return int(number, base=3)


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(2)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("10")
