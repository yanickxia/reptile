# -*- coding:utf-8 -*-

from datetime import date, timedelta

f = open("calender.sql", "w")

sql = """
INSERT INTO P2P_CALENDAR (P2P_DATE, IS_HOLIDAY, FUND_INCOME, YIELD, CREATED_AT, UPDATED_AT, IS_COMPANY_HOLIDAY) SELECT TO_DATE('{0}', 'YYYY-MM-DD HH24:MI:SS'), 0, NULL, NULL, sysdate, sysdate, 0 FROM dual WHERE NOT exists(SELECT 1 FROM P2P_CALENDAR WHERE P2P_DATE = TO_DATE('{1}', 'YYYY-MM-DD HH24:MI:SS'));
"""

start_date = date(2014, 1, 1)
i = 0
while True:
    today = (start_date + timedelta(days=i))

    time_d = today.strftime('%Y-%m-%d %H:%M:%S')
    i += 1

    if today >= date(2017, 12, 31):
        break

    f.write(sql.format(time_d, time_d))
