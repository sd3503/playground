# -*- coding: utf-8 -*-


def solution(my_string, indices):

    return "".join(x for i, x in enumerate(my_string) if i not in indices)


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("programmers")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3])
