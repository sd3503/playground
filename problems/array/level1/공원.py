# -*- coding: utf-8 -*-


def validation(matSize, park, i, j):
    lineSize = len(park)
    tileSize = len(park[0])

    if lineSize <= i + matSize - 1 or tileSize <= j + matSize - 1:
        return False
    for di in range(i, i + matSize, 1):
        for dj in range(j, j + matSize, 1):
            if park[di][dj] != "-1":
                return False

    return True


def solution(mats, park):
    smats = sorted(mats, reverse=True)

    for matSize in smats:
        for i, line in enumerate(park):
            for j, tile in enumerate(line):
                if park[i][j] == "-1":
                    if validation(matSize, park, i, j):
                        return matSize
    return -1


if __name__ == "__main__":
    # mats, park = [5, 3, 2], [
    #     ["A", "A", "-1", "B", "B", "B", "B", "-1"],
    #     ["A", "A", "-1", "B", "B", "B", "B", "-1"],
    #     ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
    #     ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
    #     ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
    #     ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
    # ]
    mats, park = [1], [["A", "-1"]]
    print(f"Input: mats, park={mats, park} \n  Output: {solution(mats, park)}")
    solution(mats, park)
