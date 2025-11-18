# -*- coding: utf-8 -*-


def solution(date1, date2):
    return 1 if date1 < date2 else 0


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(1)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([1024, 10, 24], [1024, 10, 24])
