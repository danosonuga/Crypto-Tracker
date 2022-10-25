import pymysql
import time
import datetime
from datetime import timedelta as td
import pandas as pd
from fetchDateRange import fetchMinutesDateRange


# fetchDb - Fetch Price Data from the Binance_bot Database
def fetch15Db():
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="binance_bot" )
    cursor = connection.cursor()

    daytime_p = datetime.datetime.now()
    today = daytime_p.strftime('%Y-%m-%d %H:%M:%S')

    daytime_past = daytime_p - td(days=14)
    dayAgo = daytime_past.strftime('%Y-%m-%d %H:%M:%S')

    db_call = fetchMinutesDateRange(start_date=daytime_past, end_date=daytime_p, breakdown=24, connection=connection)

    return db_call