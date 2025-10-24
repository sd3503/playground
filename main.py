# -*- coding: utf-8 -*-
import sys
import io

# 출력 인코딩을 UTF-8로 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# 각 카테고리별 문제 import
from problems.array.two_sum import solution as array_solution
from problems.string.valid_parentheses import solution as string_solution
from problems.math.fibonacci import solution as math_solution


def main():
    """메인 함수 - 카테고리별 문제 실행"""
    print("=== 코딩테스트 연습 ===")
    print()

    # Array 문제
    print("1. Array 문제 - Two Sum")
    print("-" * 30)
    array_solution()
    print()

    # String 문제
    print("2. String 문제 - Valid Parentheses")
    print("-" * 30)
    string_solution()
    print()

    # Math 문제
    print("3. Math 문제 - Fibonacci")
    print("-" * 30)
    math_solution()
    print()


if __name__ == "__main__":
    main()
