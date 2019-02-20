import pandas as pd
import pyodbc

# This line ensures that the connection closes after running the connection string
pyodbc.pooling = False

class SQLServer_connection:

    def __init__(self,sql_code):
        self.sql_code = sql_code

    def db_connect(self, run_date = None):
        self.run_date = run_date
        # parameters to pass to the connection string for connecting to the database
        connection_variables = {'DRIVER':'{SQL Server}',
                                'SERVER':'RMB-PPR-GNVA01',
                                'DATABASE':'Geneva_data',
                                'PWD':"Academia2020!",
                                'PORT':'1433',
                                'trusted_connection':'yes'}

        try:
            # connection string to be passed into pyodbc
            connection_string = ('DRIVER='+connection_variables['DRIVER']+';SERVER='+connection_variables['SERVER']+
                                 ';PORT='+connection_variables['PORT']+';DATABASE='+connection_variables['DATABASE']+
                                 ';trusted_connection='+connection_variables['trusted_connection']+';PWD='+connection_variables['PWD'])

            # open database connection using the connection string
            conn = pyodbc.connect(connection_string)

            if run_date != None:
                # if pull the data for a specified date
                # the date will be stored in the param variable
                # note that the date should be in the same format as stored in the database
                param = [self.run_date]
                data = pd.read_sql(self.sql_code,conn,params=param)
                # close connection
                conn.close()
                return data
            else:
                # cursor.execute(self.sql_code)
                # Fetch all the data
                # data = cursor.fetchall()
                data = pd.read_sql(self.sql_code,conn)
                # close connection
                conn.close()
                return print(data)
        except:
            print("Connection unsuccessful.\n"
                  "Check if you have entered the correct information for database connection string.")



#######################################################################################################################
#                       Example of how to use the code                                                                #
#######################################################################################################################

# running the sql code without the date specified
# Type your SQL code below
sql_code = ('''SELECT *\
               FROM INSERT_YOUR_TABLE_NAME\
               WHERE INSERT_WHERE_CLAUSE
            ''')
connection = SQLServer_connection(sql_code)
data = connection.db_connect()

# if you want to pull data for a specified date
sql_code2 = ('''SELECT *\
               FROM INSERT_YOUR_TABLE_NAME\
               WHERE INSERT_WHERE_CLAUSE AND DATE_VARIABLE = CAST (? AS datetime)
            ''')
date_example = '2019/02/19'

connection = SQLServer_connection(sql_code2)
data2 = connection.db_connect(date_example)
