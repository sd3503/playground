# -*- coding: utf-8 -*-


def solution(numLog):
    result = ""
    for i in range(0, len(numLog) - 1, 1):
        data = numLog[i + 1] - numLog[i]

        if data == 1:
            result += "w"
        if data == -1:
            result += "s"
        if data == 10:
            result += "d"
        if data == -10:
            result += "a"

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("wsdawsdassw")

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])
