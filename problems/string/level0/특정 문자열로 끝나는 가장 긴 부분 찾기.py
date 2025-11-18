# -*- coding: utf-8 -*-


def solution(myString, pat):
    temp = []
    for i, x in enumerate(myString):
        if x == pat[0]:
            if pat in myString[i:]:
                temp.append(i + len(pat) - 1)

    return myString[: max(temp) + 1]


def customPrint(*args):

    req_out = "AbCdE"

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
    customPrint("AbCdEFG", "dE")
