# -*- coding: utf-8 -*-


def solution(rank, attendance):
    my_dict = {}
    for i, x in enumerate(rank):
        if attendance[i]:
            my_dict[i] = x
    a, b, c = sorted(my_dict.items(), key=lambda x: x[1])[:3]
    result = a[0] * 10000 + b[0] * 100 + c[0]
    return result


def customPrint(*args):

    req_out = 20403

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
    customPrint([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False])
