# -*- coding: utf-8 -*-


def solution(myString):

    return myString.lower().replace("a", "A")


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("AbstrAct AlgebrA")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("abstract algebra")
