# -*- coding: utf-8 -*-
"""
문제 설명
  정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

제한사항
  0 ≤ start_num ≤ end_num ≤ 50
입출력 예
  start_num	end_num	result
  3	10	[3, 4, 5, 6, 7, 8, 9, 10]
"""


def count_up(start_num, end_num):
    temp_count = []
    for i in range(start_num, end_num + 1, 1):
        temp_count.append(i)
    return temp_count
    # return list(range(start_num, end_num + 1))


def solution(start_num, end_num):
    """문제 해결 함수"""

    print(f"Input: start_num={start_num} end_num={end_num}")
    print(f"Output: {count_up(start_num, end_num)}")
    return count_up(start_num, end_num)


if __name__ == "__main__":
    start_num, end_num = 3, 10
    solution(start_num, end_num)
