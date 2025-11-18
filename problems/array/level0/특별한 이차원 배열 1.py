# -*- coding: utf-8 -*-


def solution(num):
    count = 0
    result = []
    for i in range(0, num, 1):
        result.append([])
        for j in range(0, num, 1):
            if count == j:
                result[i].append(1)
            else:
                result[i].append(0)
        count += 1

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(
        [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
        ]
    )

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(6)
