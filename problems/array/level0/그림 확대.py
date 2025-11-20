# -*- coding: utf-8 -*-


def solution(picture, k):
    result = []
    for i in range(len(picture) * k):
        result.append("")
        for j in range(len(picture[i // k]) * k):
            result[i] += picture[i // k][j // k]

    return result


def customPrint(*args):

    req_out = [
        "..xxxx......xxxx..",
        "..xxxx......xxxx..",
        "xx....xx..xx....xx",
        "xx....xx..xx....xx",
        "xx......xx......xx",
        "xx......xx......xx",
        "..xx..........xx..",
        "..xx..........xx..",
        "....xx......xx....",
        "....xx......xx....",
        "......xx..xx......",
        "......xx..xx......",
        "........xx........",
        "........xx........",
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
    customPrint(
        [
            ".xx...xx.",
            "x..x.x..x",
            "x...x...x",
            ".x.....x.",
            "..x...x..",
            "...x.x...",
            "....x....",
        ],
        2,
    )
