# -*- coding: utf-8 -*-


def solution(n, slicer, num_list):
    if n == 1:
        return num_list[: slicer[1] + 1]
    if n == 2:
        return num_list[slicer[0] :]
    if n == 3:
        return num_list[slicer[0] : slicer[1] + 1]
    if n == 4:
        return num_list[slicer[0] : slicer[1] + 1 : slicer[2]]


def customPrint(*args):

    req_out = [2, 3, 4, 5, 6]

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
    customPrint(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9])
