# -*- coding: utf-8 -*-


def solution(id_list, report, k):
    # 1. 신고처리
    # 2. 차단처리된 사람 신고자에게 이메일 송부

    # 필요 데이터 : 인원별 신고당한 횟수, 인원별 누구를 신고했는지 정보 -> 인원별 메일 수신 횟수

    re_set = set(report)
    re_count_dic = {x: 0 for x in id_list}
    re_list_dic = {x: "" for x in id_list}
    result = []
    for i in re_set:
        reported = i.split(" ")[1]
        re_count_dic[reported] += 1
    for i in re_set:
        report1 = i.split(" ")[0]
        reported = i.split(" ")[1]
        re_list_dic[report1] += " " + reported

    for i, x in enumerate(re_list_dic.keys()):
        result.append(0)
        for j in re_list_dic[x].split():
            if re_count_dic[j] >= k:
                result[i] += 1

    return result


def custeomPrint(*args):
    print("Input:")
    print(args)

    print("requrire_output:")
    print("[2, 1, 1, 0]")

    print("isCurrect:")
    print(solution(*args))


if __name__ == "__main__":
    args = (
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
    custeomPrint(*args)
    solution(*args)
