# -*- coding: utf-8 -*-


def solution(arr, queries):

    for query in queries:
        for i in range(query[0], query[1] + 1):
            arr[i] += 1

    return arr


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([1, 3, 4, 4, 4])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([0, 1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]])
