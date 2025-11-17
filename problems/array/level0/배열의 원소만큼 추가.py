# -*- coding: utf-8 -*-
def solution(arr):
    # [x for i in range(0, x, 1) for x in arr]

    return [x for x in arr for i in range(x)]


if __name__ == "__main__":
    arr = [5, 1, 4]
    print(f"Input: number={arr} \n  Output: {solution(arr)}")
    solution(arr)
