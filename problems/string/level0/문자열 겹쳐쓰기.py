# -*- coding: utf-8 -*-


def solution(my_string, overwrite_string, s):
    result = ""
    s_end = len(overwrite_string) + s - 1
    result += my_string[:s]
    result += overwrite_string
    result += my_string[s_end + 1 :]

    return result


def customPrint(*args):

    req_out = "HelloWorld"

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
    customPrint("He11oWor1d", "lloWorl", 2)
