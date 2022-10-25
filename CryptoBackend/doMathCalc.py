import pymysql
import time
import datetime
from datetime import timedelta as td
import pandas as pd

def doCalc(data, new_startdate, new_enddate):
    df = pd.DataFrame(data, columns = ['id' ,'symbol', 'price', 'calcTime'])

    #Highest and Lowest Values
    highestValue = df['price'].max()

    lowestValue = df['price'].min()

    #Mean Value
    meanValue = round(df['price'].mean(), 2)

    #Standard Deviation
    standardDev = round(df['price'].std(), 2)

    #Variant
    variant = round(df['price'].var(), 2)

    #Open and Closed Value
    # openVal = df['price'].head(1)
    openVal = df[:1]['price'][:1]
    for i in openVal:
        openVal = i

    closeVal = df['price'].tail(1)
    for i in closeVal:
        closeVal = i

    calc_data = {'highestValue': highestValue, 'lowestValue': lowestValue, 
                    'meanValue': meanValue, 'standardDev': standardDev,
                    'variant': variant, 'openVal': openVal, 'closeVal': closeVal,
                    'startDate': new_startdate, 'endDate': new_enddate
                }
    return calc_data