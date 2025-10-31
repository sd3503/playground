# -*- coding: utf-8 -*-
"""
문제 설명
    정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

제한사항
    2 ≤ num_list의 길이 ≤ 10
    1 ≤ num_list의 원소 ≤ 9
    num_list에는 적어도 한 개씩의 짝수와 홀수가 있습니다.
입출력 예
    num_list	        result
    [3, 4, 5, 2, 1]	    393
    [5, 7, 8, 3]	    581

"""


def template(num_list):
    result = 0
    odds = [str(x) for x in num_list if x % 2 == 1]
    evens = [str(x) for x in num_list if x % 2 == 0]

    return int("".join(odds)) + int("".join(evens))

    # 비트연산(가장 빠름)
    odds = []
    evens = []
    for x in num_list:
        if x & 1:  # x % 2 == 1보다 빠름
            odds.append(str(x))
        else:
            evens.append(str(x))
    return int("".join(odds)) + int("".join(evens))

    # 제너레이터 + join(메모리 최적화)
    odds = "".join(str(x) for x in num_list if x % 2 == 1)
    evens = "".join(str(x) for x in num_list if x % 2 == 0)
    return int(odds) + int(evens)


def solution(num_list):
    """문제 해결 함수"""

    print(f"Input: num_list={num_list}")
    print(f"Output: {template(num_list)}")
    return template(num_list)


if __name__ == "__main__":
    num_list = [3, 4, 5, 2, 1]
    solution(num_list)
    num_list = [5, 7, 8, 3]
    solution(num_list)
