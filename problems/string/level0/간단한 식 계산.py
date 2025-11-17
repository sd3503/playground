# -*- coding: utf-8 -*-


def solution(binomial):

    temp = binomial.split()
    num1 = int(temp[0])
    operation = temp[1]
    num2 = int(temp[2])

    result = 0

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        result = num1 / num2
    return result

    # num1, op, num2 = binomial.split()
    # operations = {
    #     "+": lambda x, y: x + y,
    #     "-": lambda x, y: x - y,
    #     "*": lambda x, y: x * y,
    #     "/": lambda x, y: x / y
    # }
    # return operations[op](int(num1), int(num2))


if __name__ == "__main__":
    binomial = "43 + 12"
    print(f"Input: number={binomial} \n  Output: {solution(binomial)}")
    solution(binomial)
