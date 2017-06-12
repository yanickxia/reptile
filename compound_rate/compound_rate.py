# coding=UTF8


def compound_rate():
    moth_principal = int(input("input every moth Principal \n"))
    goal_year = int(input("input your goal year \n"))
    goal_rate = float(input("input your goal rate \n"))

    moth_rate = goal_rate / 100 / 12
    i = 0
    total = moth_principal
    while i < goal_year * 12:
        i += 1
        print("total ", i, total)
        total = total * (1 + moth_rate)
        total += moth_principal


if __name__ == '__main__':
    compound_rate()
