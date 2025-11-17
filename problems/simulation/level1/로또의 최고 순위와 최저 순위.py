# -*- coding: utf-8 -*-


def solution(lottos, win_nums):

    win_count = 0
    for x in win_nums:
        if x in lottos:
            win_count += 1
    max_count = win_count + lottos.count(0)
    min_count = win_count

    max_point = 6 if max_count <= 0 else 7 - max_count
    min_point = 6 if min_count <= 0 else 7 - min_count

    return [max_point, min_point]


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([3, 5])

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
