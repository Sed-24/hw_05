

def generator_numbers(text: str):
    num = [float(n) for n in text.split()]
    return print(num)


text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")


print(generator_numbers(text))