import pymysql
import time
import datetime
from datetime import timedelta as td
import pandas as pd
from doMathCalc import doCalc

def fetchHourDateRange(start_date, end_date, breakdown, connection):
    new_startdate = start_date.strftime('%Y-%m-%d %H:%M:%S')
    new_enddate1 = start_date + td(hours= breakdown)
    new_enddate = new_enddate1.strftime('%Y-%m-%d %H:%M:%S')
    end_date_f = end_date.strftime('%Y-%m-%d %H:%M:%S')
    
    myCalc = []

    while new_enddate != end_date_f:
        select1 = "SELECT * FROM price WHERE calcTime BETWEEN '%s' AND '%s'" % (new_startdate, new_enddate)
        data = pd.read_sql_query(select1, connection)
        
        myCalc.append(doCalc(data, new_startdate, new_enddate))

        new_startdate_f = datetime.datetime.strptime(new_enddate, '%Y-%m-%d %H:%M:%S')
        new_enddate1 = new_startdate_f + td(hours=breakdown)

        new_startdate = new_startdate_f.strftime('%Y-%m-%d %H:%M:%S')
        new_enddate = new_enddate1.strftime('%Y-%m-%d %H:%M:%S')

    return myCalc

def fetchMinutesDateRange(start_date, end_date, breakdown, connection):
    new_startdate = start_date.strftime('%Y-%m-%d %H:%M:%S')
    new_enddate1 = start_date + td(minutes= breakdown)
    new_enddate = new_enddate1.strftime('%Y-%m-%d %H:%M:%S')
    end_date_f = end_date.strftime('%Y-%m-%d %H:%M:%S')
    myCalc = []

    while new_enddate != end_date_f:
        select1 = "SELECT * FROM price WHERE calcTime BETWEEN '%s' AND '%s'" % (new_startdate, new_enddate)
        data = pd.read_sql_query(select1, connection)
        
        myCalc.append(doCalc(data, new_startdate, new_enddate))

        new_startdate_f = datetime.datetime.strptime(new_enddate, '%Y-%m-%d %H:%M:%S')
        new_enddate1 = new_startdate_f + td(minutes=breakdown)

        new_startdate = new_startdate_f.strftime('%Y-%m-%d %H:%M:%S')
        new_enddate = new_enddate1.strftime('%Y-%m-%d %H:%M:%S')

    return myCalc