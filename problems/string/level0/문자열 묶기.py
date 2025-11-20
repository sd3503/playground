# -*- coding: utf-8 -*-


def solution(strArr):

    my_dict = {}
    for a in strArr:
        my_dict[len(a)] = my_dict.get(len(a), 0) + 1

    return max(my_dict.values())


def customPrint(*args):

    req_out = 2

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
    customPrint(["a", "bc", "d", "efg", "hi"])
