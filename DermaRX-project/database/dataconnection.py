import mysql.connector

class databaseconnection:
    # connect to database
    
            def __init__(self):
                self.connection = mysql.connector.connect(
                user = 'root',
                password = 'root',
                host = 'localhost',
                database = 'Dermarx')

                print("Connection to db is:",self.connection)
                cursorObject = self.connection.cursor()
                self.connection.commit()
                cursorObject.close()

            def get_connection(self):
                if not self.connection.is_connected():
                    self.connection.reconnect()
                return self.connection
d1 = databaseconnection()