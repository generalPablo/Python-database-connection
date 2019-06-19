"""
Created on 2019-01-16
@author: Paballo Nhambiri
paballonhambiri@gamil.com
This module is intended to define database connection to sybase
"""
import pandas as pd
import pyodbc
from pwd import getpass as pwd
# This line ensures that the connection closes after running the connection string
pyodbc.pooling = False

# Ask the user for a password to connect to the FICC PB database
db_pwd = pwd()

class FiccDatabase:

    def __init__(self,sql_code):
        self.sql_code = sql_code
    # Connect string to the database
    def db_connect(self, run_date = None):
        self.run_date = run_date
        # parameters to pass to the connection string for connecting to the database
        connection_variables = {'DRIVER':'{DriverDetail}',
                                'SERVER':'HostDetails',
                                'DATABASE':'DatebaseName',
                                'UID':'UserName',
                                'PWD':"",
                                'PORT':'Port number'}
        
       
        # print("Welcome:", connection_variables['UID'])
        # print("Welcome:", getpass.getuser())

        connection_variables['PWD'] = db_pwd
        # print("Password is:", connection_variables['PWD'])

        try:
            # connection string to be passed to pyodbc
            connection_string = ('DRIVER='+connection_variables['DRIVER']+';SERVER='+connection_variables['SERVER']+';PORT='+connection_variables['PORT']+';DATABASE='+connection_variables['DATABASE']+';UID='+connection_variables['UID']+';PWD='+connection_variables['PWD'])

            # open database connection
            conn = pyodbc.connect(connection_string)

            if run_date != None:
                # execute the sql code
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
                return data
        except pyodbc.ProgrammingError:
            print("This exception is raised of programming errors.\n\
            e.g table not found, error in mysql syntax, wrong number of parameters specified etc")
        except pyodbc.InterfaceError:
            print("When database connection fails for some reason, database will raise an InterfaceError.\n\
            Note InterfaceError only get raise when there is internal problem in connection to the database.")
        except pyodbc.OperationalError:
            print("This exception is raised for things that are not in control of the programmer.\n\
            For e.g unexpected disconnect, error in memory allocation etc, selected database not exists.")
        except:
            print("Connection unsuccessful.\n\
            Check if you have entered the correct information for database connection string.")