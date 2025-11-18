# -*- coding: utf-8 -*-


def solution(names):
    return [names[x] for x in range(0, len(names), 5)]


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(["nami", "vex"])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"])
