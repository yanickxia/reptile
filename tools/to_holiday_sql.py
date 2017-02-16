# -*- coding:utf-8 -*-

import requests
from datetime import date, timedelta
import calendar

f = open("holiday.sql", "w")


def add_months(dt, months):
    month = dt.month - 1 + months
    year = dt.year + month / 12
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


def find_holiday_in_2017():
    """
    :param x: string
    :return:
    """
    s = ""
    start_date = date(2017, 1, 1)
    for i in range(0, 12):
        s += add_months(start_date, i).strftime("%Y-%m") + ','
    return requests.get("http://www.easybots.cn/api/holiday.php?m=" + s)


def find_holiday_in(n):
    """
    :param x: string
    :return:
    """
    s = ""
    start_date = date(n, 1, 1)
    for i in range(0, 12):
        s += add_months(start_date, i).strftime("%Y-%m") + ','
    return requests.get("http://www.easybots.cn/api/holiday.php?m=" + s)


def gen_sql():
    templdate_str = """
    UPDATE P2P_CALENDAR SET IS_COMPANY_HOLIDAY = {0} WHERE P2P_DATE = TO_DATE('{1}', 'YYYY-MM-DD HH24:MI:SS');
    """
    holidays = find_holiday_in_2017().json()
    start_date = date(2014, 1, 1)
    end_date = date(2018, 1, 1)
    while start_date != end_date:
        is_holiday = 0
        if start_date.strftime("%d") in holidays[start_date.strftime("%Y%m")]:
            is_holiday = 1
        f.write(templdate_str.format(is_holiday, start_date.strftime("%Y-%m-%d %H:%M:%S")))

        start_date += timedelta(days=1)


def gen_sql(n):
    """

    :param n: int
    year
    :return:
    """
    templdate_str = """
    UPDATE P2P_CALENDAR SET IS_COMPANY_HOLIDAY = {0} WHERE P2P_DATE = TO_DATE('{1}', 'YYYY-MM-DD HH24:MI:SS');
    """
    holidays = find_holiday_in(n).json()
    start_date = date(n, 1, 1)
    end_date = date(n+1, 1, 1)
    while start_date != end_date:
        is_holiday = 0
        if start_date.strftime("%d") in holidays[start_date.strftime("%Y%m")]:
            is_holiday = 1
        f.write(templdate_str.format(is_holiday, start_date.strftime("%Y-%m-%d %H:%M:%S")))

        start_date += timedelta(days=1)


for i in range(2014, 2018):
    gen_sql(i)
