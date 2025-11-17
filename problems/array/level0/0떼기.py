# -*- coding: utf-8 -*-
import re


def solution(n_str: str):
    return n_str.lstrip("0") or "0"


if __name__ == "__main__":
    n_str = "0010"
    print(f"Input: n_str={n_str} \n  Output: {solution(n_str)}")
    solution(n_str)
