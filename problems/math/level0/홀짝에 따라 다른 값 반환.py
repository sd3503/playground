# -*- coding: utf-8 -*-
"""
test
"""


def template(n):
    result = 0
    if n & 1:
        for i in range(1, n + 1, 2):
            result += i
    else:
        for i in range(0, n + 1, 2):
            result += i**2
    return result

    # 수학 문제면 수학을 해라~

    #     if n & 1:  # 홀수
    #     return ((n + 1) // 2) ** 2
    # else:  # 짝수
    #     k = n // 2
    #     return 2 * k * (k + 1) * (2 * k + 1) // 3


def solution(n):
    print(f"Input: number={n} \n  Output: {template(n)}")
    return template(n)


if __name__ == "__main__":
    n = 7
    solution(n)
    n = 10
    solution(n)
