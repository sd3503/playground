# -*- coding: utf-8 -*-


import xmlrpc


def solution(dartResult):

    my_array = []
    for i, x in enumerate(dartResult):
        if x >= "0" and x <= "9":
            print(my_array, x, i)
            if i >= 1 and (dartResult[i - 1] >= "0" and dartResult[i - 1] <= "9"):
                my_array[len(my_array) - 1] = 10
            else:
                my_array.append(int(x))

        elif x > "A" and x < "Z":
            if x == "S":
                my_array[len(my_array) - 1] = my_array[len(my_array) - 1] ** 1
            if x == "D":
                my_array[len(my_array) - 1] = my_array[len(my_array) - 1] ** 2
            if x == "T":
                my_array[len(my_array) - 1] = my_array[len(my_array) - 1] ** 3
        elif x == "*":
            if len(my_array) > 1:
                my_array[len(my_array) - 2] = my_array[len(my_array) - 2] * 2
            my_array[len(my_array) - 1] = my_array[len(my_array) - 1] * 2
        elif x == "#":
            my_array[len(my_array) - 1] = my_array[len(my_array) - 1] * -1

    result = sum(my_array)
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(37)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint("1D2S#10S")
