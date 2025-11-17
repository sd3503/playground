# -*- coding: utf-8 -*-
def solution(num_str):

    return sum([int(x) for x in num_str])


if __name__ == "__main__":
    num_str = "123456789"
    print(f"Input: number={num_str} \n  Output: {solution(num_str)}")
    solution(num_str)
