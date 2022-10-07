import pymysql
import time
import datetime
import pandas as pd

# fetchDb - Fetch Price Data from the Binance_bot Database
def fetchDb():
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="binance_bot" )
    cursor = connection.cursor()
    
    # Query All from the Db
    select1 = "SELECT * FROM price"

    # Running the query using Pandas to read the SQL Data
    data = pd.read_sql_query(select1, connection)
    testprice = data.price
    for i in range(0, len(testprice)):
        if i == 0:
            print("Increase of: 0%")
        elif i > 0:
            if testprice[i] > testprice[i - 1]:
                percentage = ((testprice[i] - testprice[i - 1]) / testprice[i - 1]) * 100
                print("Increase of: {}%".format(round(percentage, 2)))
            elif testprice[i] < testprice[i -1]:
                percentage = ((testprice[i] - testprice[i - 1]) / testprice[i - 1]) * 100
                print("Decrease of: {}%".format(round(percentage, 2)))
    
    # Converting the data into a data frame for Table-like presentation
    df = pd.DataFrame(data, columns = ['id' ,'symbol', 'price', 'calcTime'])
    print("\n")
    print("----------------BINANCE DATA----------------\n")
    print(df)

fetchDb()