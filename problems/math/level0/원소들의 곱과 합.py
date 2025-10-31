# -*- coding: utf-8 -*-
"""
문제 설명
    정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

제한사항
    2 ≤ num_list의 길이 ≤ 10
    1 ≤ num_list의 원소 ≤ 9
입출력 예
    num_list	        result
    [3, 4, 5, 2, 1]	    1
    [5, 7, 8, 3]	    0
"""
import math


def template(num_list):
    return 1 if sum(num_list) ** 2 > math.prod(num_list) else 0


def solution(num_list):
    """문제 해결 함수"""

    print(f"Input: num_list={num_list} ")
    print(f"Output: {template(num_list)}")
    return template(num_list)


if __name__ == "__main__":
    num_list = [3, 4, 5, 2, 1]
    solution(num_list)
    num_list = [5, 7, 8, 3]
    solution(num_list)
