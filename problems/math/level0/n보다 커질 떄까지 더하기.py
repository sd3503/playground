# -*- coding: utf-8 -*-


def solution(numbers, n):
    result = 0
    for x in numbers:
        if result + x > n:
            return result + x
        else:
            result += x

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(139)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([34, 5, 71, 29, 100, 34], 123)
