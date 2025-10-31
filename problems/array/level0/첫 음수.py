# -*- coding: utf-8 -*-
"""
문제 설명
    정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

제한사항
    5 ≤ num_list의 길이 ≤ 100
    -10 ≤ num_list의 원소 ≤ 100
입출력 예
    num_list	                    result
    [12, 4, 15, 46, 38, -2, 15]	    5
    [13, 22, 53, 24, 15, 6]	        -1

"""


def template(num_list):

    return next((i for i, x in enumerate(num_list) if x < 0), -1)


def solution(num_list):
    """문제 해결 함수"""

    print(f"Input: num_list={num_list} ")
    print(f"Output: {template(num_list)}")
    return template(num_list)


if __name__ == "__main__":
    num_list = [12, 4, 15, 46, 38, -2, 15]
    solution(num_list)
    num_list = [13, 22, 53, 24, 15, 6]
    solution(num_list)
