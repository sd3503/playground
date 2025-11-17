# -*- coding: utf-8 -*-


def getDistance(a, b, c, d):
    # print(abs(a - b) + abs(c - d))
    return abs(a - b) + abs(c - d)


def solution(numbers, hand):
    result = ""
    curr_left = 11
    curr_right = 12
    pointData = {
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2],
        0: [1, 3],
        11: [0, 3],
        12: [2, 3],
    }
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            curr_left = number
            result += "L"
        elif number == 3 or number == 6 or number == 9:
            curr_right = number
            result += "R"
        else:
            if getDistance(
                pointData[curr_left][0],
                pointData[number][0],
                pointData[curr_left][1],
                pointData[number][1],
            ) > getDistance(
                pointData[curr_right][0],
                pointData[number][0],
                pointData[curr_right][1],
                pointData[number][1],
            ):
                curr_right = number
                result += "R"

            elif getDistance(
                pointData[curr_left][0],
                pointData[number][0],
                pointData[curr_left][1],
                pointData[number][1],
            ) < getDistance(
                pointData[curr_right][0],
                pointData[number][0],
                pointData[curr_right][1],
                pointData[number][1],
            ):
                curr_left = number
                result += "L"
            else:
                if hand == "left":
                    curr_left = number
                    result += "L"
                else:
                    curr_right = number
                    result += "R"

    return result


def customPrint(*args):
    print("Input:", args)

    print("requrire_output:")
    print("LRLLLRLLRRL")

    print("output:", solution(*args))


if __name__ == "__main__":
    customPrint([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
