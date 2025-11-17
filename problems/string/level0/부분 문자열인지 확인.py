# -*- coding: utf-8 -*-


def solution(my_string, target):
    return 1 if target in my_string else 0


if __name__ == "__main__":
    str1, str2 = "banana", "ana"
    print(f"Input: str1={str1} str2={str2} \n  Output: {solution(str1, str2)}")
    solution(str1, str2)
    str1, str2 = "tbt", "tbbttb"
    print(f"Input: str1={str1} str2={str2} \n  Output: {solution(str1, str2)}")
    solution(str1, str2)
