# -*- coding: utf-8 -*-


def solution(arr, intervals):
    result = []
    for x in intervals:
        start = x[0]
        end = x[1] + 1
        result.extend(arr[start:end])
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([2, 3, 4, 1, 2, 3, 4, 5])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([1, 2, 3, 4, 5], [[1, 3], [0, 4]])
