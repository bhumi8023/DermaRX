from database.dataconnection import databaseconnection

class User:
      def __init__(self,name,phoneno,age,email,password,role_id):
            self.name = name
            self.phoneno = phoneno
            self.age = age
            self.email = email
            self.password = password
            self.role_id = role_id
 

class UserRegistration:
    def __init__(self):
        db = databaseconnection()
        self.connection = db.get_connection()
        self.cursorObject = self.connection.cursor()


   
    def menu(self):
       
        print("\n--- user menu ---")
        print("1. register user")
        print("2. login user")
       

        choice = input("enter your choice: ")

        if choice == "1":
                self.register()
        elif choice == "2":
                self.login()
        else:
            print("invalid choice, try again.")     


    def register(self):
       
        try:
            self.cursorObject.execute("""
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
            self.connection.commit()

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
            self.cursorObject.execute(query,(user.email,user.phoneno))
            result = self.cursorObject.fetchone()
            if result:
                print("User already exit")
            else:
                query = """insert into user (name,phoneno,age,email,password,role_id) VALUES (%s, %s, %s,%s,%s,%s)"""
                self.cursorObject.execute(query,(user.name, user.phoneno, user.age, user.email,user.password,user.role_id))
                self.connection.commit()
                roles = {
                1: "Customer",
                2: "Admin",
                3: "Pharmacist"}
                print(f"{roles[role_id]} registered successfully!")

            
        except:
         print("Database Error")

        finally:
           print("registeration completed")
        # create object of user
        # create database connection
        # check if email and phone no already exist 

    def login(self):
       
        try:
            print("\n***** LOGIN *****")
            print("1. Login with Phone Number")
            print("2. Login with Email")

            choice = input("Enter your choice: ")

            if choice == "1":

                phoneno = int(input("Enter phone number: "))
                password = input("Enter the password: ")
                query = """select * from user where phoneno = %s and password = %s"""
                self.cursorObject.execute(query,(phoneno,password))

            elif choice == "2":

                email = input("Enter the email: ")   
                password = input("Enter the password: ") 
                query = """select * from user where email = %s and password = %s"""
                self.cursorObject.execute(query,(email,password))
            else:
                print("Invalid choice")
                return
            result = self.cursorObject.fetchone()

            if result:
                print("Login successful!")
            else:
                print("Invalid credentials")

        except:
                print("Database Error")
        
        finally:
            print("Login completed")