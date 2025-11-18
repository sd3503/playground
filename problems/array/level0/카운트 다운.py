# -*- coding: utf-8 -*-


def solution(start_num, end_num):
    result = []

    for i in range(start_num, end_num - 1, -1):
        result.append(i)
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([10, 9, 8, 7, 6, 5, 4, 3])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(10, 3)
