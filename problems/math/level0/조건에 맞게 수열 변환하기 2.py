# -*- coding: utf-8 -*-


def solution(arr):
    data = arr[::]
    result = 0
    while True:
        for i, x in enumerate(arr):
            if x >= 50 and not x & 1:
                arr[i] = x // 2
            if x < 50 and x & 1:
                arr[i] = x * 2 + 1
        if data == arr:
            return result
        result += 1
        data = arr[::]


def customPrint(*args):

    req_out = 5

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
    customPrint([1, 2, 3, 100, 99, 98])
