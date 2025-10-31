# -*- coding: utf-8 -*-
"""
문제 설명
    문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.
제한사항
    1 ≤ my_string의 길이 ≤ 100
    my_string은 영소문자로만 이루어져 있습니다.
    1 ≤ k ≤ 100
입출력 예
    my_string	k	result
    "string"	3	"stringstringstring"
    "love"	10	"lovelovelovelovelovelovelovelovelovelove"
"""


def template(my_string, k):
    result = ""
    for i in range(0, k, 1):
        result += my_string
    return result

    # return my_string * k
    # return ''.join([my_string for _ in range(k)])


def solution(my_string, k):
    """문제 해결 함수"""

    print(f"Input: my_string={my_string} k={k}")
    print(f"Output: {template(my_string, k)}")
    return template(my_string, k)


if __name__ == "__main__":
    my_string, k = "string", 3
    solution(my_string, k)
    my_string, k = "love", 3
    solution(my_string, k)
