# -*- coding: utf-8 -*-


def solution(order):
    result = 0
    for x in order:
        if "americano" in x or x == "anything":
            result += 4500
        if "cafelatte" in x:
            result += 5000

    return result


def customPrint(*args):

    req_out = 19000

    get_out = solution(*args)
    # print("Input:", args)
    print("req_output:", req_out)
    print("get_output:", get_out)
    print(
        "------------------------success------------------------"
        if req_out == get_out
        else "------------------------fail------------------------"
    )


if __name__ == "__main__":
    customPrint(["cafelatte", "americanoice", "hotcafelatte", "anything"])
