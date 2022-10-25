import pymysql
import time
import datetime
from datetime import timedelta as td
import pandas as pd
from fetchDateRange import fetchHourDateRange

# fetchDb - Fetch Price Data from the Binance_bot Database
def fetch4Db():
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="binance_bot" )
    cursor = connection.cursor()

    daytime_p = datetime.datetime.now()
    today = daytime_p.strftime('%Y-%m-%d %H:%M:%S')

    daytime_past = daytime_p - td(days=5)
    dayAgo = daytime_past.strftime('%Y-%m-%d %H:%M:%S')

    db_call = fetchHourDateRange(start_date=daytime_past, end_date=daytime_p, breakdown=4, connection=connection)

    return db_call