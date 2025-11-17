# -*- coding: utf-8 -*-


def solution(price, money, count):
    total = 0
    for i in range(1, count + 1, 1):
        total += i * price
    if money < total:
        return total - money
    else:
        return 0


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(10)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint(3, 20, 4)
