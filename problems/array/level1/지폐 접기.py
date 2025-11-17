# -*- coding: utf-8 -*-
def validate(wallet, bill):
    walletx = wallet[0]
    wallety = wallet[1]

    billx = bill[0]
    billy = bill[1]

    return (walletx >= billx and wallety >= billy) or (
        walletx >= billy and wallety >= billx
    )


def folding(bill):
    x = bill[0]
    y = bill[1]

    if x >= y:
        x = x // 2
    else:
        y = y // 2

    return [x, y]


def solution(wallet, bill):
    count = 0

    if validate(wallet, bill):
        return count
    while True:
        print(f"Input: wallet, bill={wallet, bill}")
        bill = folding(bill)
        print(f"Input: wallet, bill={wallet, bill}")
        count += 1
        if validate(wallet, bill):
            return count


if __name__ == "__main__":
    wallet, bill = [30, 15], [26, 17]
    print(f"Input: wallet, bill={wallet, bill} \n  Output: {solution(wallet, bill)}")
    solution(wallet, bill)
