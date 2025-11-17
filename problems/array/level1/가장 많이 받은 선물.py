# -*- coding: utf-8 -*-
def getGiftPoints(friends, gifts):
    result = {}
    for frirend in friends:
        send = sum(1 for gift in gifts if gift.split(" ")[0] == frirend)
        get = sum(1 for gift in gifts if gift.split(" ")[1] == frirend)
        result[frirend] = send - get
    return result


def solution(friends, gifts):
    # 선물을 주고받은 적이 있으면 선물 더 많이 준 사람이 선물을 하나 받는다.
    # 기록이 없거나 수가 같다면, 지수가 더 큰 사람이 선물지수가 더 작은 사람에게 선물을 하나 받는다.
    # 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않는다.
    # 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return
    gift_points = getGiftPoints(friends, gifts)

    re_gift = {x: 0 for x in friends}

    for i in range(0, len(friends), 1):
        for j in range(i, len(friends), 1):
            fi = friends[i]
            fj = friends[j]
            if fi != fj:
                i_to_j = fi + " " + fj
                j_to_i = fj + " " + fi
                if gifts.count(i_to_j) > 0 or gifts.count(j_to_i) > 0:
                    if gifts.count(i_to_j) > gifts.count(j_to_i):
                        re_gift[fi] += 1
                    elif gifts.count(i_to_j) < gifts.count(j_to_i):
                        re_gift[fj] += 1
                    else:
                        if gift_points.get(fi) > gift_points.get(fj):
                            re_gift[fi] += 1
                        elif gift_points.get(fi) < gift_points.get(fj):
                            re_gift[fj] += 1
                else:
                    if gift_points.get(fi) > gift_points.get(fj):
                        re_gift[fi] += 1
                    elif gift_points.get(fi) < gift_points.get(fj):
                        re_gift[fj] += 1
    result = max(re_gift.values())
    return result


if __name__ == "__main__":
    friends, gifts = ["muzi", "ryan", "frodo", "neo"], [
        "muzi frodo",
        "muzi frodo",
        "ryan muzi",
        "ryan muzi",
        "ryan muzi",
        "frodo muzi",
        "frodo ryan",
        "neo muzi",
    ]
    print(
        f"Input: friends, gifts={friends, gifts} \n  Output: {solution(friends, gifts)}"
    )
    solution(friends, gifts)
