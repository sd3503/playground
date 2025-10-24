# -*- coding: utf-8 -*-
"""
Valid Parentheses 문제
LeetCode 20번 문제
"""

def is_valid(s):
    """
    괄호가 올바르게 닫혔는지 확인하는 함수
    
    Args:
        s: 괄호 문자열
        
    Returns:
        유효한 괄호인지 여부
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

def solution():
    """문제 해결 함수"""
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    
    for s in test_cases:
        result = is_valid(s)
        print(f"Input: '{s}'")
        print(f"Output: {result}")
        print()

if __name__ == "__main__":
    solution()
