import pymysql
import time
import datetime
from datetime import timedelta as td
import pandas as pd

# fetchDb - Fetch Price Data from the Binance_bot Database
def fetchLastHour():
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="binance_bot" )
    cursor = connection.cursor()

    daytime_p = datetime.datetime.now()
    today = daytime_p.strftime('%Y-%m-%d %H:%M:%S')

    daytime_past = daytime_p - td(hours= 1)
    hourAgo = daytime_past.strftime('%Y-%m-%d %H:%M:%S')
    
    # Query All from the Db
    select1 = "SELECT * FROM price WHERE calcTime BETWEEN '%s' AND '%s'" % (hourAgo, today)

    data = pd.read_sql_query(select1, connection)

    # Converting the data into a data frame for Table-like presentation
    df = pd.DataFrame(data, columns = ['id' ,'symbol', 'price', 'calcTime'])
    print("\n")
    print("----------------BINANCE DATA----------------\n")
    print(df)

    #Highest and Lowest Values
    print("The Maximum Price is: {}".format(df['price'].max()))
    print("The Minimum Price is: {}".format(df['price'].min()))

    #Mean Value
    print("The Mean Price is: {}".format(df['price'].mean().round(2)))

    #Standard Deviation
    print("The Standard Deviation is: {}".format(df['price'].std().round(2)))

    #Variant
    print("The Variant is: {}".format(df['price'].var().round(2)))

    #Open and Closed Value
    print("The First data is: {}".format(df.head(1)['price']))
    print("The Last data is: {}".format(df.tail(1)['price']))
fetchLastHour()