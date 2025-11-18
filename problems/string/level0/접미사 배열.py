# -*- coding: utf-8 -*-


def solution(my_string):
    result = []
    for i in range(0, len(my_string), 1):
        result.append(my_string[i:])

    return sorted(result)


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(["a", "ana", "anana", "banana", "na", "nana"])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("banana")
