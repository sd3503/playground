# -*- coding: utf-8 -*-


def solution(my_string):
    data = {}
    for i in range(ord("A"), ord("z") + 1):
        data[chr(i)] = 0
    for i in range(ord("a"), ord("z") + 1):
        data[chr(i)] = 0

    for x in my_string:
        data[x] += 1

    return list(data.values())


def customPrint(*args):

    req_out = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        1,
        0,
        0,
        3,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
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
    customPrint("Programmers")
