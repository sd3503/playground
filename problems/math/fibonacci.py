# -*- coding: utf-8 -*-
"""
Fibonacci 문제
"""


def fibonacci(n):
    """
    피보나치 수열의 n번째 수를 구하는 함수

    Args:
        n: 피보나치 수열의 인덱스

    Returns:
        n번째 피보나치 수
    """
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def solution():
    """문제 해결 함수"""
    n = 10
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")

    # 처음 10개 피보나치 수 출력
    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")


if __name__ == "__main__":
    solution()
