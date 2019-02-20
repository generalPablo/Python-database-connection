import cx_Oracle
import pandas as pd

class Oracle_Database:

    def __init__(self, hostname, db_name,port, username, password, sql_code):

        self.hostname = hostname
        self.db_name = db_name
        self.port = port
        self.username = username
        self.password = password
        self.sql_code = sql_code

    def db_connect_oracle(self, run_date):
        self.run_date = run_date
        # parameters to pass to the connection string for connecting to the database
        connection_variables = {'SERVER': self.hostname,
                                'DATABASE': self.db_name,
                                'UID': self.username,
                                'PWD': self.password,
                                'PORT': self.port}
        try:
            # connection string to be passed to oracle db
            dsn = cx_Oracle.makedsn(connection_variables['SERVER'], connection_variables['PORT'], service_name=connection_variables['DATABASE'])
            connection = cx_Oracle.Connection(user=connection_variables['UID'], password=connection_variables['PWD'], dsn=dsn)

            # creating a date parameter to be passed into the query
            param = {'rundate': self.run_date}
            # creating a dataframe

            data = pd.read_sql(self.sql_code,connection,params=param)
            # close connection
            connection.close()
            return data
        except:
            print("Connection unsuccessful.\nCheck if you have entered the correct information for database connection string.")