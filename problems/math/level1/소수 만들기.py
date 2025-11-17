# -*- coding: utf-8 -*-


def solution(nums):
    result = 0
    for i, numi in enumerate(nums):
        for j, numj in enumerate(nums[i + 1 :]):
            for k, numk in enumerate(nums[i + j + 2 :]):
                temp = numi + numj + numk
                count = 0
                for ii in range(2, temp // 2 + 1, 1):
                    if temp % ii == 0:
                        count += 1
                if count == 0:
                    result += 1

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print(4)

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint([1, 2, 7, 6, 4])
