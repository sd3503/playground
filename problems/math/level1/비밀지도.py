# -*- coding: utf-8 -*-


def to_bina_str(a1, a2, n):
    result = ""
    a1_str = ""
    a2_str = ""
    while a1 > 0:
        a1_str += str(a1 % 2)
        a1 = a1 // 2
    while a2 > 0:
        a2_str += str(a2 % 2)
        a2 = a2 // 2
    a1_str = a1_str[::-1]
    a2_str = a2_str[::-1]
    for a, b in zip(a1_str.zfill(n), a2_str.zfill(n)):
        # print(a, b)
        result += str(int(a) | int(b))
    print(a1_str, a2_str)
    return result


def solution(n, arr1, arr2):
    bina_str_arr = []
    for a1, a2 in zip(arr1, arr2):
        bina_str_arr.append(to_bina_str(a1, a2, n))

    result = []
    for bina_str in bina_str_arr:
        result.append("".join(["#" if x == "1" else " " for x in bina_str]))

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(["#####", "# # #", "### #", "#  ##", "#####"])

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
