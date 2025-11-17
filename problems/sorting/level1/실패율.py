# -*- coding: utf-8 -*-


def solution(N, stages):
    failPer = {}
    for i in range(1, N + 1, 1):
        failPer[i] = {i: 0}
    for i in failPer.keys():
        under = sum(1 for x in stages if x == i)
        over = sum(1 for x in stages if x >= i)
        if over == 0:
            failPer[i] = 0
        else:
            failPer[i] = under / over
    result = [x[0] for x in sorted(failPer.items(), key=lambda x: x[1], reverse=True)]
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([3, 4, 2, 1, 5])

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint(5, [2, 1, 2, 6, 2, 4, 3, 3])
