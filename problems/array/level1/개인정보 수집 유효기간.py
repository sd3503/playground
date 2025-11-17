# -*- coding: utf-8 -*-


def solution(today, terms, privacies):
    year, month, day = today.split(".")
    d_today = int(year) * 12 * 28 + int(month) * 28 + int(day)

    d_terms_dict = {}
    count = 1
    for term in terms:
        p_type, p_turn = term.split(" ")
        d_terms_dict[p_type] = int(p_turn) * 28

    result = []
    for private in privacies:
        private_day, private_type = private.split(" ")
        # print(private_day, private_type)

        p_year, p_month, p_day = private_day.split(".")
        private_addDay = d_terms_dict[private_type]
        p_today = int(p_year) * 12 * 28 + int(p_month) * 28 + int(p_day)

        p_today += private_addDay
        if d_today >= p_today:
            result.append(count)
        count += 1

    return result


def custeomPrint(*args):
    print(
        f"Input: {args} \n"
        + f"requrire_output: {[1, 3]} \n"
        + f"output: {solution(*args)}"
    )


if __name__ == "__main__":
    today, terms, privacies = (
        "2022.05.19",
        ["A 6", "B 12", "C 3"],
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
    )
    custeomPrint(today, terms, privacies)
    solution(today, terms, privacies)
