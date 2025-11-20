# -*- coding: utf-8 -*-


def solution(a, b):

    return str(int(a) + int(b))


def customPrint(*args):

    req_out = "305793246910280479981"

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
    customPrint("18446744073709551615", "287346502836570928366")
