# -*- coding: utf-8 -*-


def solution(arr):
    result = []
    for x in arr:
        if result and result[-1] == x:
            result.pop()
        else:
            result.append(x)

    return result or [-1]


def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]


def customPrint(*args):

    req_out = [0, 1, 0]

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
    customPrint([0, 1, 1, 1, 0])
