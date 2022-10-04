import pymysql
import time
import datetime
from datetime import timedelta as td
import pandas as pd

# fetchDb - Fetch Price Data from the Binance_bot Database
def fetchLast15Mins():
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="binance_bot" )
    cursor = connection.cursor()

    daytime_p = datetime.datetime.now()
    today = daytime_p.strftime('%Y-%m-%d %H:%M:%S')

    daytime_past = daytime_p - td(minutes= 15)
    hourAgo = daytime_past.strftime('%Y-%m-%d %H:%M:%S')
    
    # Query All from the Db
    select1 = "SELECT * FROM price WHERE calcTime BETWEEN '%s' AND '%s'" % (hourAgo, today)

    data = pd.read_sql_query(select1, connection)

    # Converting the data into a data frame for Table-like presentation
    df = pd.DataFrame(data, columns = ['id' ,'symbol', 'price', 'calcTime'])
    print("\n")
    print("----------------BINANCE DATA----------------\n")
    print(df)
fetchLast15Mins()