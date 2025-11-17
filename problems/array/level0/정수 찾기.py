# -*- coding: utf-8 -*-
def solution(num_list, n):

    return 1 if n in num_list else 0


if __name__ == "__main__":
    num_list, n = [1, 2, 3, 4, 5], 3
    print(f"Input: num_list={num_list} n={n} \nOutput: {solution(num_list, n)}")
    solution(num_list, n)
