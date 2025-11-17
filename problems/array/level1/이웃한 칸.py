# -*- coding: utf-8 -*-
def solution(board, h, w):

    count = 0
    c_co = board[h][w]

    if h > 0:
        count += 1 if c_co == board[h - 1][w] else 0
    if w > 0:
        count += 1 if c_co == board[h][w - 1] else 0
    if h < len(board) - 1:
        count += 1 if c_co == board[h + 1][w] else 0
    if w < len(board[0]) - 1:
        count += 1 if c_co == board[h][w + 1] else 0

    return count


if __name__ == "__main__":
    board, h, w = (
        [
            ["blue", "red", "orange", "red"],
            ["red", "red", "blue", "orange"],
            ["blue", "orange", "red", "red"],
            ["orange", "orange", "red", "blue"],
        ],
        1,
        1,
    )
    print(f"Input: board, h, w={board, h, w} \n  Output: {solution(board, h, w)}")
    solution(board, h, w)
