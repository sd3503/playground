# -*- coding: utf-8 -*-


def solution(num):

    return 100


def customPrint(*args):

    req_out = 100

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
    customPrint(100)
