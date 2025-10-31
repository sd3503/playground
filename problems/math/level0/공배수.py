# -*- coding: utf-8 -*-
"""
문제 설명
    정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

제한사항
    10 ≤ number ≤ 100
    2 ≤ n, m < 10
입출력 예
number	n	m	result
    60	2	3	1
    55	10	5	0

"""


def template(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0


def solution(number, n, m):
    """문제 해결 함수"""

    print(f"Input: number={number} n={n} m={m}")
    print(f"Output: {template(number, n, m)}")
    return template(number, n, m)


if __name__ == "__main__":
    number, n, m = 60, 2, 3
    solution(number, n, m)
    number, n, m = 55, 10, 5
    solution(number, n, m)
