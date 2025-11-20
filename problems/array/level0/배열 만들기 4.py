# -*- coding: utf-8 -*-


def solution(arr):
    stk = []
    for x in arr:
        while stk and stk[-1] >= x:
            stk.pop()
        if not stk or stk[-1] < x:
            stk.append(x)
    return stk


def customPrint(*args):

    req_out = [1, 2, 3]

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
    customPrint([1, 4, 2, 5, 3])
