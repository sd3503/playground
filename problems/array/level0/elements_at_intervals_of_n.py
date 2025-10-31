# -*- coding: utf-8 -*-
"""
문제 설명
  정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

제한사항
  5 ≤ num_list의 길이 ≤ 20
  1 ≤ num_list의 원소 ≤ 9
  1 ≤ n ≤ 4
입출력 예
  num_list	n	result
  [4, 2, 6, 1, 7, 6]	2	[4, 6, 7]
  [4, 2, 6, 1, 7, 6]	4	[4, 7]
"""


def elements_at_intervals_of_n(num_list, n):
    temp_list = []
    for i in range(0, len(num_list), n):
        temp_list.append(num_list[i])

    return temp_list

    # return num_list[::n]


def solution(num_list, n):
    """문제 해결 함수"""

    print(f"Input: num_list={num_list} n={n}")
    print(f"Output: {elements_at_intervals_of_n(num_list,n)}")

    return elements_at_intervals_of_n(num_list, n)


if __name__ == "__main__":
    num_list = [4, 2, 6, 1, 7, 6]
    n = 2
    solution(num_list, n)
