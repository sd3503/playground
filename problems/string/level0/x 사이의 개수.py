# -*- coding: utf-8 -*-
def solution(myString: str):

    return [len(x) for x in myString.split("x")]


if __name__ == "__main__":
    myString = "oxooxoxxox"
    print(f"Input: number={myString} \n  Output: {solution(myString)}")
    solution(myString)
