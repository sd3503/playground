# -*- coding: utf-8 -*-


def solution(myString):
    return sorted([x for x in myString.split("x") if x != ""])


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(["aaaa", "bbb", "cc", "d"])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("dxccxbbbxaaaa")
