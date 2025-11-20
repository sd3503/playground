# -*- coding: utf-8 -*-


def solution(my_string, queries):
    result = my_string
    for q in queries:
        tempStr = result[: q[0]]
        tempStr += result[q[0] : q[1] + 1][::-1]
        tempStr += result[q[1] + 1 :]
        result = tempStr

    return result


def customPrint(*args):

    req_out = "programmers"

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
    customPrint("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])
