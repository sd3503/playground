# -*- coding: utf-8 -*-


def solution(num):
    for i in range(2, num, 1):
        if num % i == 1:
            return i
    return 0


def custeomPrint(*args):
    print("Input:")
    print(args)

    print("requrire_output:")
    print("3")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    args = 10
    # custeomPrint(*args)
    solution(args)
