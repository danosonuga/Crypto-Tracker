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
    # Converting the data into a data frame for Table-like presentation
    df = pd.DataFrame(data, columns = ['id' ,'symbol', 'price', 'calcTime'])
    print("\n")
    print("----------------BINANCE DATA----------------\n")
    print(df)

fetchDb()