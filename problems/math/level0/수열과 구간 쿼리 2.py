# -*- coding: utf-8 -*-


def solution(arr, queries):
    result = []
    for s, e, k in queries:
        result.append(min((x for x in arr[s : e + 1] if x > k), default=-1))

    return result


def customPrint(*args):

    req_out = [3, 4, -1]

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
    customPrint([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]])
