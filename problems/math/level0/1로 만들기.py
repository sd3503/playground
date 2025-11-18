# -*- coding: utf-8 -*-


def solution(num_list):
    result = 0
    for num in num_list:
        while num > 1:
            num = num // 2
            result += 1

    return result


def customPrint(*args):

    req_out = 11

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
    customPrint([12, 4, 15, 1, 14])
