# -*- coding: utf-8 -*-


def solution(my_string, m, c):
    result = ""
    for i in range(0, len(my_string), m):
        if len(my_string) - 1 >= i + c - 1:
            result += my_string[i + c - 1]

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("happy")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint("ihrhbakrfpndopljhygc", 4, 2)
