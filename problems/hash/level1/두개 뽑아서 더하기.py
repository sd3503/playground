# -*- coding: utf-8 -*-


def solution(numbers):
    my_dict = {}
    for i, x in enumerate(numbers):

        for y in numbers[i + 1 :]:
            print(x, y)
            my_dict[x + y] = my_dict.get(x + y, 0)
    result = sorted(my_dict.keys())

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print([2, 3, 4, 5, 6, 7])

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint([2, 1, 3, 4, 1])
