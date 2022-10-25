import pymysql
import time
import datetime
from price import binance_qry
from datetime import timedelta as td
import threading

# insertDB - Inserts Data from Binance Price_Data API into the Db asynchonously
def insertDb():
    #database connection
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="binance_bot" )
    cursor = connection.cursor()
    # some other statements  with the help of cursor

    data_list = []
    BASE_URL = "https://api.binance.com"
    API_KEY = "eba2hrjHECrvuHsG6UTpcEYcPKjE6wi1HtOwixM4lb9REq3iaT4mIjepW90nnyCB"
    symbol = "ETHBUSD"

    i = 0
    while i < 10:
        newdata = binance_qry(BASE_URL, symbol, API_KEY)
        data_list.append(newdata)
        time.sleep(1)
        i += 1
    
    for data in data_list:
        symbol1 = data["symbol"]
        price1 = data["price"]
        calcTime1 = data["calcTime"]

        calcTime = calcTime1 + 3600000


        s, ms = divmod(calcTime1, 1000)
        formatTime1 = str('%s.%03d' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(s)), ms)).split('.')[0]

        insert1 = "INSERT INTO price(symbol,price,calcTime) VALUES('%s', '%s', '%s')" % (symbol1, price1, formatTime1)
        cursor.execute(insert1)
    connection.commit()
    connection.close()

# setInterval - Sets the interval for the API to get queried
#       and be inserted into the DB
def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()    

setInterval(insertDb, 0)