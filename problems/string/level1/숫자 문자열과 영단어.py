# -*- coding: utf-8 -*-


def solution(s):

    my_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for x in my_dict.keys():
        s = s.replace(x, my_dict[x])
    result = int(s)
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(1478)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint("one4seveneight")
