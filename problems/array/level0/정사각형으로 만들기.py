# -*- coding: utf-8 -*-


def solution(arr):
    low = len(arr)
    col = len(arr[0])

    max1 = max(low, col)
    result = arr[::]
    for i in result:
        for j in range(max1 - col):
            i.append(0)
    for i in range(max1 - low):
        result.append([0] * max1)

    return result


def customPrint(*args):

    req_out = [
        [572, 22, 37, 0],
        [287, 726, 384, 0],
        [85, 137, 292, 0],
        [487, 13, 876, 0],
    ]

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
    customPrint([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]])
