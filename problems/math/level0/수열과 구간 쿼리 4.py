# -*- coding: utf-8 -*-


def solution(arr, queries):
    data = arr[::]
    for q in queries:
        for i, x in enumerate(arr[q[0] : q[1] + 1]):
            if (q[0] + i) % q[2] == 0:
                data[q[0] + i] += 1

    return data


def customPrint(*args):

    req_out = [3, 2, 4, 6, 4]

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
    customPrint([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]])
