# -*- coding: utf-8 -*-
def solution(data, ext, val_ext, sort_by):
    data_index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    # print(data_index[ext])

    result = sorted(
        [x for x in data if x[data_index[ext]] < val_ext],
        key=lambda x: x[data_index[sort_by]],
    )

    return result


if __name__ == "__main__":
    data, ext, val_ext, sort_by = (
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "date",
        20300501,
        "remain",
    )
    print(
        f"Input: {data, ext, val_ext, sort_by} \n  Output: {solution(data, ext, val_ext, sort_by)}"
    )
    solution(data, ext, val_ext, sort_by)
