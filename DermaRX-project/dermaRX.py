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
                if not self.connection.is_connected():
                    self.connection.reconnect()
                return self.connection
d1 = databaseconnection()

class User:
      def __init__(self,name,phoneno,age,email,password,role_id):
            self.name = name
            self.phoneno = phoneno
            self.age = age
            self.email = email
            self.password = password
            self.role_id = role_id
 

class UserRegistration:

    def register(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:
            cursorObject.execute("""
                            CREATE TABLE if not exists User(
                            user_id INT AUTO_INCREMENT PRIMARY KEY,
                            role_id INT,
                            name VARCHAR(255) ,
                            email VARCHAR(255) ,
                            age INT not null, 
                            phoneno INT not null,
                            password varchar(225),
                            FOREIGN KEY (role_id) REFERENCES role(role_id)
                            )
                        """)
            connection.commit()

            name = input("Enter the name: ")
            phoneno = int(input("Enter the phoneno: "))
            age = int(input("Enter the age: "))
            email = input("Enter the email-id: ")
            password = input("Enter the password: ")
            print("\nSelect Role:")
            print("1. Customer")
            print("2. Admin")
            print("3. Pharmacist")

            role_id = int(input("Enter the role id: "))
            if role_id not in [1, 2, 3]:
                        print("Invalid role selected!")
                        return
            user = User(name,
                        phoneno,
                        age,
                        email,
                        password,
                        role_id)
            
            query ="""select * from user where email=%s OR phoneno=%s"""
            cursorObject.execute(query,(user.email,user.phoneno))
            result = cursorObject.fetchone()
            if result:
                print("User already exit")
            else:
                query = """insert into user (name,phoneno,age,email,password,role_id) VALUES (%s, %s, %s,%s,%s,%s)"""
                cursorObject.execute(query,(user.name, user.phoneno, user.age, user.email,user.password,user.role_id))
                connection.commit()
                roles = {
                1: "Customer",
                2: "Admin",
                3: "Pharmacist"}
                print(f"{roles[role_id]} registered successfully!")

            cursorObject.close()
        except:
         print("Database Error")

        finally:
            cursorObject.close()
        # create object of user
        # create database connection
        # check if email and phone no already exist 

    def login(self):
        connection = d1.get_connection()
        phoneno = int(input("Enter the phoneno: "))
        email = input("Enter the email-id: ")
        password = input("Enter the password: ")
        cursorObject = connection.cursor()
<<<<<<< HEAD
        phoneno = int(input("Enter the phoneno: "))
        email = input("Enter the email-id: ")
        query = """select * from user where email =%s and phoneno = %s"""
        cursorObject.execute(query,(email,phoneno))
=======
        query = """select * from user where email =%s and phoneno = %s and password = %s"""
        cursorObject.execute(query,(email,phoneno,password))
>>>>>>> 85198b4 (Add role selection and fix database connection)
        result = cursorObject.fetchone()
        if result:
            print("Login successful!")
        else:
            print("Invalid credentials")
        cursorObject.close()


ur1 = UserRegistration()
<<<<<<< HEAD
ur1.register()
<<<<<<< HEAD
ur1.login()
=======
ur1.login()
>>>>>>> a3be98a (Add new project features)
=======
print("\n*****DERMA-RX******")
print("1. Register")
print("2. Login")
choice = input("\nEnter your choice: ")
if choice == "1":
    ur1.register()

elif choice == "2":
    ur1.login()
>>>>>>> 85198b4 (Add role selection and fix database connection)
