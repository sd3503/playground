# -*- coding: utf-8 -*-
"""
문제 설명
    정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.

제한사항
    2 ≤ num_list의 길이 ≤ 10
    1 ≤ num_list의 원소 ≤ 9
입출력 예
    num_list	    result
    [2, 1, 6]	    [2, 1, 6, 5]
    [5, 2, 1, 7, 5]	[5, 2, 1, 7, 5, 10]
"""


def template(num_list):
    result = num_list.copy()
    last = num_list[len(num_list) - 1]
    lastb1 = num_list[len(num_list) - 2]
    if last > lastb1:
        result.append(last - lastb1)
    else:
        result.append(last * 2)
    return result


def solution(a, b, flag):
    """문제 해결 함수"""

    print(f"Input: num_list={num_list}")
    print(f"Output: {template(num_list)}")
    return template(num_list)


if __name__ == "__main__":
    num_list = [2, 1, 6]
    solution(num_list)
