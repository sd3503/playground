# -*- coding: utf-8 -*-
def solution(strArr):

    return [x.upper() if i & 1 else x.lower() for i, x in enumerate(strArr)]


if __name__ == "__main__":
    strArr = ["AAA", "BBB", "CCC", "DDD"]
    print(f"Input: number={strArr} \n  Output: {solution(strArr)}")
    solution(strArr)
