# -*- coding: utf-8 -*-


def solution(survey, choices):
    result_dict = {}
    for i, x in enumerate(survey):
        if choices[i] <= 4:
            result_dict[x[0]] = result_dict.get(x, 0) + (4 - choices[i])
        else:
            result_dict[x[1]] = result_dict.get(x, 0) + choices[i] - 4
    test_dict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}

    for key1, value1 in result_dict.items():
        for key2, value2 in test_dict.items():
            if key2[0] == key1:
                test_dict[key2] -= value1
            elif key2[1] == key1:
                test_dict[key2] += value1
    result = []
    for key2, value2 in test_dict.items():
        if value2 > 0:
            result.append(key2[1])
        elif value2 < 0:
            result.append(key2[0])
        else:
            result.append(key2[0])

    return "".join(result)


def custeomPrint(*args):
    print(
        f"Input: {args} \n"
        + f"requrire_output: {args} \n"
        + f"output: {solution(*args)}"
    )


if __name__ == "__main__":
    survey, choices = ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
    custeomPrint(survey, choices)
    solution(survey, choices)
