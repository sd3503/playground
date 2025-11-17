# -*- coding: utf-8 -*-
def solution(num_list):
    return sorted(num_list)[5:]


if __name__ == "__main__":
    num_list = [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]
    print(f"Input: num_list={num_list} \n  Output: {solution(num_list)}")
    solution(num_list)
