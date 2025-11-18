# -*- coding: utf-8 -*-


def solution(n, k):
    result = []
    for i in range(k, n + 1, k):
        result.append(i)

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([3, 6, 9])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(15, 5)
