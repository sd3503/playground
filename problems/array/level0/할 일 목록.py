# -*- coding: utf-8 -*-


def solution(todo_list, finished):
    result = []

    for todo, finish in zip(todo_list, finished):
        if not finish:
            result.append(todo)

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(["practiceguitar", "studygraph"])

    print("output:")
    print(solution(*args))


if __name__ == "__main__":
    customPrint(
        ["problemsolving", "practiceguitar", "swim", "studygraph"],
        [True, False, True, False],
    )
