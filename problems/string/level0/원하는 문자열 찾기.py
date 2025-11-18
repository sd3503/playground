# -*- coding: utf-8 -*-


def solution(myString, pat):

    return 1 if pat.lower() in myString.lower() else 0


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(1)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("AbCdEfG", "aBc")
