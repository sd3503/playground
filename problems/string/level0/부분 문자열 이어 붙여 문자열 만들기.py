# -*- coding: utf-8 -*-


def solution(my_strings, parts):
    result = ""
    for my_srt, part in zip(my_strings, parts):
        result += my_srt[part[0] : part[1] + 1]

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("programmers")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(
        ["progressive", "hamburger", "hammer", "ahocorasick"],
        [[0, 4], [1, 2], [3, 5], [7, 7]],
    )
