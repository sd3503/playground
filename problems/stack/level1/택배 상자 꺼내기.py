# -*- coding: utf-8 -*-
"""
test
"""


def getYX(num, w):
    y = int((num - 1) / w)
    index_in_layer = (num - 1) % w

    if y & 1:
        x = w - 1 - index_in_layer
    else:
        x = index_in_layer
    return x, y


def template(n, w, num):
    target_x, target_y = getYX(num, w)  # 언패킹
    last_x, last_y = getYX(n, w)  # 언패킹
    result = last_y - target_y

    if last_y & 1:
        result += 1 if last_x <= target_x else 0
    else:
        result += 1 if last_x >= target_x else 0

    return result


def solution(n, w, num):
    print(f"Input: n, w, num={n, w, num} \n  Output: {template(n, w, num)}")
    return template(n, w, num)


if __name__ == "__main__":
    n, w, num = 22, 6, 8
    solution(n, w, num)
