# -*- coding: utf-8 -*-


def solution(q, r, code):
    result = ""
    for i, x in enumerate(code):
        if i % q == r:
            result += x

    return result


def customPrint(*args):

    req_out = "jerry"

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
    customPrint(3, 1, "qjnwezgrpirldywt")
