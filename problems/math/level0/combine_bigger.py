# -*- coding: utf-8 -*-
"""
문제 설명
  연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
  12 ⊕ 3 = 123
  3 ⊕ 12 = 312
  양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

  단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
제한사항
    1 ≤ a, b < 10,000
입출력 예
    a	b	result
    9	91	991
    89	8	898
"""


def combine_bigger(a, b):

    str_a = str(a)
    str_b = str(b)

    str_ab = str_a + str_b
    str_ba = str_b + str_a

    if int(str_ab) >= int(str_ba):
        return int(str_ab)
    else:
        return int(str_ba)
    # 한줄로
    # return max(int(str(a) + str(b)), int(str(b) + str(a)))


def solution(a, b):
    """문제 해결 함수"""

    print(f"Input: a={a} b={b}")
    print(f"Output: {combine_bigger(a, b)}")

    return combine_bigger(a, b)


if __name__ == "__main__":
    solution(1, 23)
