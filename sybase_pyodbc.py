import pandas as pd
import pyodbc
import getpass

# This line ensures that the connection closes after running the connection string
pyodbc.pooling = False

class Sybase_connection:

    def __init__(self,sql_code):
        self.sql_code = sql_code

    def db_connect(self, run_date = None):
        self.run_date = run_date
        # parameters to pass to the connection string for connecting to the database
        connection_variables = {'DRIVER':'{Adaptive Server Enterprise}',
                                'SERVER':'DBMS20',
                                'DATABASE':'RFDS',
                                'UID':"",
                                'PWD':"",
                                'PORT':'5000'}

        connection_variables['UID'] = getpass.getuser().lower()
        print("Welcome:", connection_variables['UID'])
        connection_variables['PWD'] = getpass.getpass(prompt='Password:',stream=None)
        print("Password is:", connection_variables['PWD'])

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
                return print(data)
        except pyodbc.ProgrammingError as err:
            # This exception is raised of programming errors.
            # For e.g table not found, error in mysql syntax, wrong number of parameters specified etc
            print(err)
        except pyodbc.InterfaceError as err:
            # When database connection fails for some reason, MySQLdb will raise an InterfaceError.
            # Note InterfaceError only get raise when there is internal problem in connection to the database,
            # MySQLdb will not raise InterfaceError because of wrong database name or password.
            print(err)
        except pyodbc.OperationalError as err:
            # This exception is raised for things that are not in control of the programmer.
            # For e.g unexpected disconnect, error in memory allocation etc, selected database not exists.
            print(err)
        except:
            print("Connection unsuccessful.\nCheck if you have entered the correct information for database connection string.")