# -*- coding: utf-8 -*-


def solution(intStrs, k, s, l):
    result = []

    for ist in intStrs:
        idata = int(ist[s : s + l])
        if idata > k:
            result.append(idata)

    return result


def customPrint(*args):

    req_out = [56789, 99999]

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
    customPrint(["0123456789", "9876543210", "9999999999999"], 50000, 5, 5)
