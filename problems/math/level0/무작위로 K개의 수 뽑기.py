# -*- coding: utf-8 -*-


def solution(arr, k):

    result = []
    for a in arr:
        if a not in result:
            result.append(a)
        if len(result) >= k:
            break
    result += [-1] * (k - len(result))

    return result


def customPrint(*args):

    req_out = [0, 1, 2]

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
    customPrint([0, 1, 1, 2, 2, 3], 3)
