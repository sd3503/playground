# -*- coding: utf-8 -*-
"""
코딩테스트 연습
코딩 기초 트레이닝 2번 문제
레벨0
n 번째 원소부터
"""


def from_the_nth_element(num_list, n):
    """
    정수 리스트 num_list와 정수 n이 주어질 때,
    n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.

    제한사항
        2 ≤ num_list의 길이 ≤ 30
        1 ≤ num_list의 원소 ≤ 9
        1 ≤ n ≤ num_list의 길이

    입출력 예
        num_list	    n	result
        [2, 1, 6]	    3	[6]
        [5, 2, 1, 7, 5]	2	[2, 1, 7, 5]
    """
    return num_list[n - 1 :]


def solution(num_list, n):
    """문제 해결 함수"""
    print(f"Input: num_list = {num_list}, n = {n}")
    print(f"Output: {from_the_nth_element(num_list, n)}")
    return from_the_nth_element(num_list, n)


if __name__ == "__main__":
    solution([2, 1, 6], 3)
    solution([5, 2, 1, 7, 5], 2)
