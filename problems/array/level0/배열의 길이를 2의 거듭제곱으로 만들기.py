# -*- coding: utf-8 -*-


def solution(arr):
    t_num = 1
    result = []
    while t_num < len(arr):
        t_num *= 2

    for i in range(t_num):
        if i <= len(arr) - 1:
            result.append(arr[i])
        else:
            result.append(0)

    return result


def customPrint(*args):

    req_out = [1, 2, 3, 4, 5, 6, 0, 0]

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
    customPrint([1, 2, 3, 4, 5, 6])
