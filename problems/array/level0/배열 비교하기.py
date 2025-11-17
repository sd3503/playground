# -*- coding: utf-8 -*-
def solution(arr1, arr2):
    tuple1 = (len(arr1), sum(arr1))
    tuple2 = (len(arr2), sum(arr2))

    if tuple1 > tuple2:
        return 1
    elif tuple1 < tuple2:
        return -1
    else:
        return 0


if __name__ == "__main__":
    arr1, arr2 = [49, 13], [70, 11, 2]
    print(f"Input: arr1, arr2={arr1, arr2} \n  Output: {solution(arr1, arr2)}")
    solution(arr1, arr2)
