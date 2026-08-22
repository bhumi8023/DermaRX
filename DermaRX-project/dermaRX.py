import mysql.connector

class databaseconnection:
    # connect to databa
    
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
                return self.connection

d1 = databaseconnection()

class User:
      def __init__(self,name,phoneno,age,email):
            self.name = name
            self.phoneno = phoneno
            self.age = age
            self.email = email

    

class UserRegistration:

    def register(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        cursorObject.execute("""
                        CREATE TABLE if not exists User(
                        name VARCHAR(255) ,
                        email VARCHAR(255) ,
                        age INT not null, 
                        phoneno INT not null
                        )
                    """)
        connection.commit()

        name = input("Enter the name: ")
        phoneno = int(input("Enter the phoneno: "))
        age = int(input("Enter the age: "))
        email = input("Enter the email-id: ")
        user = User(name,
                    phoneno,
                    age,
                    email)
        
        query ="""select * from user where email=%s OR phoneno=%s"""
        cursorObject.execute(query,(user.email,user.phoneno))
        result = cursorObject.fetchone()
        if result:
            print("User already exit")
        else:
            query = """insert into user (name,phoneno,age,email) VALUES (%s, %s, %s,%s)"""
            cursorObject.execute(query,(user.name, user.phoneno, user.age, user.email))
            connection.commit()
            print("User registered successfully!")
        cursorObject.close()

        # create object of user
        # create database connection
        # check if email and phone no already exist 

    def login(self,email,phoneno):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        query = """select * from user where email =%s and phoneno = %s"""
        cursorObject.execute(query,(email,phoneno))
        result = cursorObject.fetchone()
        if result:
            print("Login successful!")
        else:
            print("Invalid credentials")
        cursorObject.close()


ur1 = UserRegistration()
ur1.register()
ur1.login('siya@123',982365745)