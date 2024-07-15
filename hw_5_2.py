import re

Text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")


def generator_numbers(text: str):
    yield re.findall(r'\s\d[\d.,]*\s', text)


def sum_profit(text, generator):
    total = 0
    for i in generator(text):
        for j in i:
            total += float(j)
    return total


print(sum_profit(Text, generator_numbers))
