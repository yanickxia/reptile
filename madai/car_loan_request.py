# coding=UTF8

import requests

URL = "https://www.madailicai.com/p2p/service/carLoans"


def count_for_car_loan():
    params = {"productType": "CAR_LOAN_REQUEST"}
    result = requests.head(url=URL, params=params)
    return result.headers.get('X-Record-Count')


def list_of_car_loan(start, size):
    params = {"from": start, "productType": "CAR_LOAN_REQUEST", "size": size}
    result = requests.get(url=URL, params=params)
    return result.json()


count_car_loan = count_for_car_loan()
all_car_loan = list_of_car_loan(0, count_car_loan)

sum_of_money = 0
for car_loan in all_car_loan:
    sum_of_money += car_loan['currentInvestmentAmount']

print(sum_of_money)