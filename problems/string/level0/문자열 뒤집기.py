# -*- coding: utf-8 -*-


def solution(my_string, s, e):
    result = ""
    result += my_string[:s]
    result += (my_string[s : e + 1 : 1])[::-1]
    result += my_string[e + 1 :]

    return result


def customPrint(*args):

    req_out = "ProgrammerS123"

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
    customPrint("Progra21Sremm3", 6, 12)
