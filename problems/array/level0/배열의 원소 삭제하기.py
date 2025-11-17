# -*- coding: utf-8 -*-
def solution(arr, delete_list):
    # 서순이 안된다!
    # return list(set(arr) - set(delete_list))
    return [x for x in arr if x not in delete_list]


if __name__ == "__main__":
    arr, delete_list = [293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]
    print(
        f"Input: arr={arr} delete_list={delete_list} \n  Output: {solution(arr, delete_list)}"
    )
    solution(arr, delete_list)
