# -*- coding: utf-8 -*-


def solution(code):
    ret = []
    mode = 0
    for i, x in enumerate(code):
        if x == "1":
            mode = int(not mode)
        elif not mode and not i & 1:
            ret.append(x)
        elif mode and i & 1:
            ret.append(x)

    return "".join(ret) or "EMPTY"


def customPrint(*args):

    req_out = "acbac"

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
    customPrint("abc1abc1abc")
