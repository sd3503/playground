# -*- coding: utf-8 -*-


def solution(a, b, c, d):
    data = (a, b, c, d)
    myDict = {}
    for x in data:
        myDict[x] = myDict.get(x, 0) + 1
    myDict = dict(sorted(myDict.items(), key=lambda x: -x[1]))
    if len(myDict) == 1:
        return a * 1111
    if len(myDict) == 2:
        p, q = myDict.keys()
        if 1 in myDict.values():
            return (10 * p + q) ** 2
        else:
            return (p + q) * abs(p - q)
    if len(myDict) == 3:
        q, r = [x[0] for x in myDict.items() if x[1] == 1]
        return q * r
    if len(myDict) == 4:
        return min(a, b, c, d)


def customPrint(*args):

    req_out = 2222

    get_out = solution(*args)
    # print("Input:", args)
    print("req_output:", req_out)
    print("get_output:", get_out)
    print(
        "------------------------success------------------------"
        if req_out == get_out
        else "------------------------fail------------------------"
    )


if __name__ == "__main__":
    customPrint(2, 2, 2, 2)
