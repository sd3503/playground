# -*- coding: utf-8 -*-


def solution(l, r):
    result = []
    for i in range(l, r + 1):
        if not str(i).replace("0", "").replace("5", ""):
            result.append(i)

    return result or [-1]


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
    customPrint(5, 555)
