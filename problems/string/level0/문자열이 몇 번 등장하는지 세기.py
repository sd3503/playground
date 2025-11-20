# -*- coding: utf-8 -*-


def solution(myString, pat):
    result = 0
    for i, c in enumerate(myString):
        if c == pat[0]:
            if myString[i : i + len(pat)] == pat:
                result += 1
    return result


def customPrint(*args):

    req_out = 2

    get_out = solution(*args)
    # print("Input:", args)
    print("req_output:", req_out)
    print("get_output:", get_out)
    print(
        "------------------------success------------------------"
        if req_out == get_out
        else "------------------------fail------------------------"
    )


if __name__ == "__main__":
    customPrint("banana", "ana")
