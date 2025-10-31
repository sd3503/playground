# -*- coding: utf-8 -*-
"""
문제 설명
  정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.

제한사항
  2 ≤ num_list의 길이 ≤ 30
  1 ≤ num_list의 원소 ≤ 9
  1 ≤ n ≤ num_list의 길이 ___
입출력 예
  num_list	n	result
  [2, 1, 6]	1	[2]
  [5, 2, 1, 7, 5]	3	[5, 2, 1]

"""


def n_번째_원소까지(num_list, n):

    return num_list[:n]


def solution(num_list, n):
    """문제 해결 함수"""

    print(f"Input: num_list={num_list} n={n}")
    print(f"Output: {n_번째_원소까지(num_list,n)}")
    return n_번째_원소까지(num_list, n)


if __name__ == "__main__":
    num_list = [5, 2, 1, 7, 5]
    n = 3
    solution(num_list, n)
