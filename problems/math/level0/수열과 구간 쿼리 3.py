# -*- coding: utf-8 -*-


def solution(arr, queries):

    for q in queries:
        arr[q[0]], arr[q[1]] = arr[q[1]], arr[q[0]]

    return arr


def customPrint(*args):

    req_out = [3, 4, 1, 0, 2]

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
    customPrint([0, 1, 2, 3, 4], [[0, 3], [1, 2], [1, 4]])
