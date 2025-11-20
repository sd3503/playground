# -*- coding: utf-8 -*-


def solution(myStr):

    data = ["a", "b", "c"]

    for d in data:
        myStr = myStr.replace(d, ",")
    result = [x for x in myStr.split(",") if x]

    return result or ["EMPTY"]


def customPrint(*args):

    req_out = ["onlettu", "etom", "to"]

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
    customPrint("baconlettucetomato")
