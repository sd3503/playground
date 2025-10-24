# -*- coding: utf-8 -*-
"""
Two Sum 문제
LeetCode 1번 문제
"""

def two_sum(nums, target):
    """
    두 수의 합이 target이 되는 인덱스를 찾는 함수
    
    Args:
        nums: 정수 배열
        target: 목표 합
        
    Returns:
        두 인덱스의 리스트
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

def solution():
    """문제 해결 함수"""
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Explanation: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}")

if __name__ == "__main__":
    solution()
