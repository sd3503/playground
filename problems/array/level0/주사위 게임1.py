# -*- coding: utf-8 -*-
def solution(a, b):
    if a & 1 and b & 1:
        return a**2 + b**2
    elif a & 1 or b & 1:
        return (a + b) * 2
    else:
        return abs(a - b)


if __name__ == "__main__":
    a, b = 3, 5
    print(f"Input: a, b={a, b} \n  Output: {solution(a, b)}")
    solution(a, b)
