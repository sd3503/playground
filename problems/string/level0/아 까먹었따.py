# -*- coding: utf-8 -*-


def solution(str1, str2):
    return 1 if str1 in str2 else 0


if __name__ == "__main__":
    str1, str2 = "abc", "aabcc"
    print(f"Input: str1={str1} str2={str2} \n  Output: {solution(str1, str2)}")
    solution(str1, str2)
    str1, str2 = "tbt", "tbbttb"
    print(f"Input: str1={str1} str2={str2} \n  Output: {solution(str1, str2)}")
    solution(str1, str2)
