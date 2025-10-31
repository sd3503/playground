# -*- coding: utf-8 -*-
"""
문제 설명
    문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
    my_string은 숫자와 알파벳으로 이루어져 있습니다.
    1 ≤ my_string의 길이 ≤ 1,000
    1 ≤ n ≤ my_string의 길이
입출력 예
    my_string	n	result
    "ProgrammerS123"	11	"grammerS123"
    "He110W0r1d"	5	"W0r1d"
"""


def template(my_string, n):
    return my_string[-n:]


def solution(my_string, n):
    """문제 해결 함수"""

    print(f"Input: my_string={my_string} n={n} ")
    print(f"Output: {template(my_string, n)}")
    return template(my_string, n)


if __name__ == "__main__":
    my_string, n = "ProgrammerS123", 11
    solution(my_string, n)
