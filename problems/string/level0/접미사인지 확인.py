# -*- coding: utf-8 -*-


def solution(my_string: str, is_suffix):

    if my_string.endswith(is_suffix):
        return 1
    else:
        return 0


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(1)

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("banana", "ana")
