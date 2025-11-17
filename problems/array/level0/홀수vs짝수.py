# -*- coding: utf-8 -*-
def solution(num_list):
    return max(
        sum([x for i, x in enumerate(num_list) if i & 1]),
        sum([x for i, x in enumerate(num_list) if not (i & 1)]),
    )

    #   슬라이싱을 사용하자!
    # return max(sum(num_list[::2]), sum(num_list[1::2]))


if __name__ == "__main__":
    num_list = [4, 2, 6, 1, 7, 6]
    print(f"Input: number={num_list} \n  Output: {solution(num_list)}")
    solution(num_list)
