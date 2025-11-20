# -*- coding: utf-8 -*-


def solution(x1, x2, x3, x4):

    return (x1 or x2) and (x3 or x4)


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
    customPrint(False, True, True, True)
