# -*- coding: utf-8 -*-


def solution(myStr):

    for i, x in enumerate(myStr):
        if x == "l":
            return myStr[:i]
        elif x == "r":
            return myStr[i + 1 :]
    return []


def customPrint(*args):

    req_out = ["u", "u"]

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
    customPrint(["u", "u", "l", "r"])
