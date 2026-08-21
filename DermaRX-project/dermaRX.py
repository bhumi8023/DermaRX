import mysql.connector

class databaseconnection:
    # connect to databa
    def __init__(self):
        try:
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
                return self.connection
        
        except:
            print("Can't connect to database")

        finally:
            print("Closing connection")   
d1 = databaseconnection
class user:

    def __init__(self,name,phoneno,age,email):
        self.name = name
        self.phoneno = phoneno
        self.age = age
        self.email = email

class UserRegistration:

    def register(self):
        pass
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        
        # create object of user
        # create database connection
        # check if email and phone no already exist 

    def login(self):
        pass
