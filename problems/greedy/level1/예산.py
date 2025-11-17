# -*- coding: utf-8 -*-


def solution(d, budget):
    result = 0
    for x in sorted(d):
        if budget - x >= 0:
            budget -= x
        else:
            break
        result += 1

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(3)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([1, 3, 2, 5, 4], 9)
