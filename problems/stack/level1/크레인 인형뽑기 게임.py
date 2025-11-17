# -*- coding: utf-8 -*-


def solution(board, moves):
    my_array = []
    result = 0
    for move in moves:
        for tail in board:
            if tail[move - 1] != 0:
                my_array.append(str(tail[move - 1]))
                tail[move - 1] = 0
                if len(my_array) >= 2:
                    if my_array[len(my_array) - 1] == my_array[len(my_array) - 2]:
                        result += 2
                        my_array = my_array[:-2]
                break

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(4)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
