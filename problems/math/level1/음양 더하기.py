# -*- coding: utf-8 -*-


def solution(absolutes, signs):
    result = 0
    for i, sign in zip(absolutes, signs):
        if sign:
            result += i
        else:
            result -= i

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(9)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint([4, 7, 12], [True, False, True])
