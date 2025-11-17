# -*- coding: utf-8 -*-
def solution(strArr):

    return [x for x in strArr if "ad" not in x]


if __name__ == "__main__":
    strArr = ["and", "notad", "abcd"]
    print(f"Input: number={strArr} \n  Output: {solution(strArr)}")
    solution(strArr)
