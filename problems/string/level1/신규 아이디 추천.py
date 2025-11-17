# -*- coding: utf-8 -*-


def solution(new_id: str):
    result = ""
    new_id = new_id.lower()
    for x in new_id:
        if (
            (x >= "a" and x <= "z")
            or (x >= "0" and x <= "9")
            or x == "-"
            or x == "_"
            or x == "."
        ):
            result += x
    while ".." in result:
        result = result.replace("..", ".")
    if result.startswith("."):
        result = result[1:]
    if result.endswith("."):
        result = result[:-1]
    if not result:
        result = "a"
    if len(result) > 15:
        result = result[:15]
    if result.endswith("."):
        result = result[:-1]
    while len(result) <= 2:
        result += result[len(result) - 1]
    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("abcdefghijklmn")

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint("abcdefghijklmn.p")
