# -*- coding: utf-8 -*-


def solution(num_list):
    result = 0
    if len(num_list) >= 11:
        for x in num_list:
            result += x
    else:
        result = 1
        for x in num_list:
            result *= x

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(51)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1])
