import pymysql
import time
import datetime
from datetime import timedelta as td
import pandas as pd

# fetchDb - Fetch Price Data from the Binance_bot Database
def fetchLastDay():
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="binance_bot" )
    cursor = connection.cursor()

    daytime_p = datetime.datetime.now()
    today = daytime_p.strftime('%Y-%m-%d %H:%M:%S')

    daytime_past = daytime_p - td(hours= 24)
    dayAgo = daytime_past.strftime('%Y-%m-%d %H:%M:%S')
    
    # Query All from the Db
    select1 = "SELECT * FROM price WHERE calcTime BETWEEN '%s' AND '%s'" % (dayAgo, today)

    data = pd.read_sql_query(select1, connection)

    # Converting the data into a data frame for Table-like presentation
    df = pd.DataFrame(data, columns = ['id' ,'symbol', 'price', 'calcTime'])
    print("\n")
    print("----------------BINANCE DATA----------------\n")
    print(df)
fetchLastDay()