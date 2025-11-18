# -*- coding: utf-8 -*-


def solution(board, moves):
    stack = []
    result = 0
    for move in moves:
        idx = move - 1
        for row in board:
            if row[idx] != 0:
                cur_dol = row[idx]
                row[idx] = 0
                if stack and stack[-1] == cur_dol:
                    result += 2
                    stack.pop()
                else:
                    stack.append(cur_dol)
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
