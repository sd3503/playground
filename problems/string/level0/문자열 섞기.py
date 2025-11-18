# -*- coding: utf-8 -*-


def solution(str1, str2):
    result = ""
    for s1, s2 in zip(str1, str2):
        result += s1 + s2
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("ababababab")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("aaaaa", "bbbbb")
