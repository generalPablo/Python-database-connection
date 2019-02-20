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

    def db_connect_oracle(self, run_date=None):
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
            if run_date != None:
                param = {'rundate': self.run_date}
                # creating a dataframe

                data = pd.read_sql(self.sql_code,connection,params=param)
                # close connection
                connection.close()
                return data
            else:
                data = pd.read_sql(self.sql_code, connection)
                # close connection
                connection.close()
                return data
        except:
            print("Connection unsuccessful.\n"
                  "Check if you have entered the correct information for database connection string.")


#######################################################################################################################
#                       Example of how to use the code                                                                #
#######################################################################################################################

# Example 1 - case where you pull data for a specific date
# SQL code should look like the below

sql_code = ('''SELECT INSERT_COLUMN_NAMES\
                FROM INSERT_TABLE_NAME\
                WHERE BUSINESSDATE =: rundate
                ''')
# notice that rundate is variable that we will bind to the query
# Hence we defined a binding variable inside our class param = {'rundate': self.run_date}
# You can extend the parameters, e.g if you might want to put two dates to get a range of data.
# You will need to modify the code in the Class above


conn = Oracle_Database("Host name or server","Database name", "port number", "username", "password",sql_code)

date_example = '20190219'
data = conn.db_connect_oracle(date_example)

# Example 2 -  If no date is provided, then call the method as follows
data2 = conn.db_connect_oracle()
