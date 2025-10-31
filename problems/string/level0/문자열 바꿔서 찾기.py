# -*- coding: utf-8 -*-
"""
문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.
"""


def template(myString, pat):
    result = ""

    myString = myString.translate(str.maketrans({"A": "B", "B": "A"}))

    return 1 if pat in myString else 0


def solution(myString, pat):
    print(f"Input: myString={myString} pat={pat} \nOutput: {template(myString, pat)}")
    return template(myString, pat)


if __name__ == "__main__":
    myString, pat = "ABBAA", "AABB"
    solution(myString, pat)

    myString, pat = "ABAB", "ABAB"
    solution(myString, pat)
