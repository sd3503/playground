# -*- coding: utf-8 -*-
def solution(bandage, health, attacks):
    comboCount = 0
    current_health = health
    attacks_dict = {}
    for attack in attacks:
        attacks_dict[attack[0]] = attack[1]
    for t in range(0, attacks[len(attacks) - 1][0] + 1, 1):
        if attacks_dict.get(t, 0):
            comboCount = 0
            current_health -= attacks_dict[t]
            if current_health <= 0:
                return -1
        else:
            comboCount += 1
            current_health += bandage[1]
            if comboCount >= bandage[0]:
                current_health += bandage[2]
                comboCount = 0
            if current_health > health:
                current_health = health
        print(current_health)

    return current_health


if __name__ == "__main__":
    bandage, health, attacks = [5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]
    print(
        f"Input: bandage, health, attacks={bandage, health, attacks} \n  bandage, health, attacks: {solution(bandage, health, attacks)}"
    )
    solution(bandage, health, attacks)
