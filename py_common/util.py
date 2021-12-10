#coding: utf8

import datetime
import time

def get_date():
    now = int(time.time())
    time_struct = time.localtime(now)
    return time.strftime("%Y%m%d", time_struct)

def get_day_before(day):
    return (datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%d")


