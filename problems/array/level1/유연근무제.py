# -*- coding: utf-8 -*-
"""
test
"""
import sys
import io

# Windows 콘솔 한글 출력 설정
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def getHM(time, addData):

    time += addData
    if (time % 100) // 60 >= 1:
        time = (time + 100) // 100 * 100 + time % 100 % 60
    return time


def template(schedules, timelogs, startday):
    count = 0
    flag = True
    for sch, timelog in zip(schedules, timelogs):
        add_sch = getHM(sch, 10)
        for i, my_time in enumerate(timelog):
            if my_time > add_sch and ((startday - 1 + i) % 7) < 5:
                flag = False
                break
        if flag:
            count += 1
        flag = True

    return count


def solution(schedules, timelogs, startday):
    return template(schedules, timelogs, startday)


if __name__ == "__main__":
    # 테스트 케이스 1: 기본 케이스
    # 예상 결과: 계산 필요 (실행 후 확인)
    schedules, timelogs, startday = (
        [700, 800, 1100],
        [
            [700, 1111, 1111, 700, 700, 700, 700],
            [800, 800, 800, 800, 800, 800, 800],
            [1105, 1105, 1105, 1105, 1105, 1105, 1105],
        ],
        5,
    )
    print("=== Test Case 1: Basic ===")
    result1 = solution(schedules, timelogs, startday)
    print(f"Result: {result1}\n")
