# -*- coding: utf-8 -*-


def solution(arr, query):
    for i, q in enumerate(query):
        if not i & 1:
            arr = arr[0 : q + 1]
        else:
            arr = arr[q:]

    return arr


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
    customPrint([0, 1, 2, 3, 4, 5], [4, 1, 2])
