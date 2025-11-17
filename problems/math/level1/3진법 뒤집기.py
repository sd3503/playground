# -*- coding: utf-8 -*-


def solution(n):
    tryple = 0
    count = 0
    while 3**count <= n:
        tryple += ((n % (3 ** (count + 1))) // 3**count) * 10**count
        count += 1
    temp = str(tryple)
    result = 0
    for i, x in enumerate(temp):
        result += int(x) * 3**i

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(1)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint(9)
