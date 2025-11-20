# -*- coding: utf-8 -*-


def solution(ineq, eq, n, m):

    if ineq == "<":
        if eq == "=":
            return int(n <= m)
        else:
            return int(n < m)
    else:
        if eq == "=":
            return int(n >= m)
        else:
            return int(n > m)


def customPrint(*args):

    req_out = 1

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
    customPrint("<", "=", 20, 50)
