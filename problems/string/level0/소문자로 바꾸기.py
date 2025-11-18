# -*- coding: utf-8 -*-


def solution(myString):

    return myString.lower()


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("abcdefg")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("aBcDeFg")
