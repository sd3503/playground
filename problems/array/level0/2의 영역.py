# -*- coding: utf-8 -*-


def solution(arr):

    if 2 not in arr:
        return [-1]
    test = [i for i, x in enumerate(arr) if x == 2]
    return arr[test[0] : test[-1] + 1]


def customPrint(*args):

    req_out = [2, 1, 4, 5, 2]

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
    customPrint([1, 1, 1])
