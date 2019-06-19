"""
This module is designed to load data into the FICC PB database
"""
import csv
import os
import pyodbc
import pandas as pd

pyodbc.pooling = False
connection = pyodbc.connect('DSN=DSNNAME;UID=UserName;PWD=Password')
cursor = connection.cursor()


# Method 1
file_name = 'pb_client_list'
location = os.getcwd() + '\\' + file_name +'.csv'

with open(location,'r') as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        cursor.execute("INSERT INTO client_list VALUES (?,?,?,?,?)",row)

connection.commit()
cursor.close()

