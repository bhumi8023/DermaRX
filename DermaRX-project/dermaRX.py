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

d1 = databaseconnection()
class user:

    def __init__(self,name,phoneno,age,email):
        self.name = name
        self.phoneno = phoneno
        self.age = age
        self.email = email

class UserRegistration:

    def register(self):
       
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        cursorObject.execute("select * from users where email=%s OR phoneno=%s", (user.email, user.phoneno))
        result = cursorObject.fetchone()
        if result:
            print("User already exit")
        else:
            cursorObject.execute("INSERT INTO Student1 (name,phoneno, email, age) VALUES (%s, %s, %s,%s)" ,
                (user.name, user.phoneno, user.age, user.email))    
            connection.commit()
            print("User registered successfully!")
        cursorObject.close()

        # create object of user
        # create database connection
        # check if email and phone no already exist 

    def login(self,email,phoneno):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        cursorObject.execute("select * from user where email =%s and phoneno = %s",(email,phoneno))
        result = cursorObject.fetchone()
        if result:
            print("Login successful!")
        else:
            print("Invalid credentials")
        cursorObject.close()
