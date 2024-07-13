import re

text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")


def generator_numbers(text: str):
    return [float(n) for n in text.split() if re.search(r'\d[\d.,]*', n)]


def sum_profit(num):
    return sum(num)


print(sum_profit(generator_numbers(text)))
