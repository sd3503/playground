# -*- coding: utf-8 -*-
"""
test
"""


def toSec(text):
    m, s = map(int, text.split(":"))
    return m * 60 + s


def toText(sec):
    m = sec // 60
    s = sec % 60
    return f"{m:02d}:{s:02d}"


def template(video_len, pos, op_start, op_end, commands):
    video_len_sec, pos_sec, op_start_sec, op_end_sec = (
        toSec(video_len),
        toSec(pos),
        toSec(op_start),
        toSec(op_end),
    )
    # 오프닝 건너뛰기
    if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    for command in commands:
        if command == "next":
            pos_sec += 10
            if pos_sec > video_len_sec:
                pos_sec = video_len_sec
        if command == "prev":
            pos_sec -= 10
            if pos_sec < 0:
                pos_sec = 0
        if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return toText(pos_sec)


def solution(video_len, pos, op_start, op_end, commands):
    print(
        f"Input: video_len, pos, op_start, op_end, commands={video_len, pos, op_start, op_end, commands} \n  Output: {template(video_len, pos, op_start, op_end, commands)}"
    )
    return template(video_len, pos, op_start, op_end, commands)


if __name__ == "__main__":
    video_len, pos, op_start, op_end, commands = (
        "34:33",
        "13:00",
        "00:55",
        "02:55",
        ["next", "prev"],
    )
    solution(video_len, pos, op_start, op_end, commands)
