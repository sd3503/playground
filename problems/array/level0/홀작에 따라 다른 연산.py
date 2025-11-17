# -*- coding: utf-8 -*-
def solution(arr, n):
    return (
        [x if index & 1 else x + n for index, x in enumerate(arr)]
        if len(arr) & 1
        else [x + n if index & 1 else x for index, x in enumerate(arr)]
    )


if __name__ == "__main__":
    arr, n = [49, 12, 100, 276, 33], 27
    print(f"Input: arr={arr} n={n} \n  Output: {solution(arr, n)}")
    solution(arr, n)
    arr, n = [444, 555, 666, 777], 100
    print(f"Input: arr={arr} n={n} \n  Output: {solution(arr, n)}")
    solution(arr, n)
