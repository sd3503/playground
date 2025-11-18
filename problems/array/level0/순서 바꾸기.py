# -*- coding: utf-8 -*-


def solution(num_list, n):
    result = []
    result.extend(num_list[n:])
    result.extend(num_list[:n])
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([1, 6, 2])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([2, 1, 6], 1)
