from database.dataconnection import databaseconnection


class Profiledetails:

    def __init__(self,user_id,firstname,lastname,dob,gender):
            self.user_id = user_id
            self.firstname = firstname
            self.lastname = lastname
            self.dob = dob
            self.gender = gender
            # self.address = address
           
class Profile:

    def create_profile(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:

            user_id = int(input("Enter the user_id: "))

            query = """select * from user where user_id = %s """
            cursorObject.execute(query,(user_id,))
            result = cursorObject.fetchone()

            if result is None:
                print("User ID  not found!")
                return
            
            firstname = input("Enter the firstname: ")
            lastname = input("Enter the lastname: ")
            dob = input("Enter the date of birth: ")
            gender = input("Enter the gender: ")
            # address = input("Enter the address: ")
            profile = Profiledetails(
                user_id,
                firstname,
                lastname,
                dob,
                gender
            )
            query = """insert into profile (user_id,firstname,lastname,dob,gender) VALUES (%s, %s, %s,%s,%s)"""
            cursorObject.execute(query,(profile.user_id,profile.firstname,profile.lastname,profile.dob,profile.gender))
            connection.commit()
            print("Profile created successfully!")

        except mysql.connector.Error as e:
            print("Database Error:", e)

        finally:
            cursorObject.close()

    def read(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:
            self.user_id = int(input("Enter the user_id: "))
            query = """select profile.firstname , profile.lastname,profile.dob,profile.gender,user.phoneno,user.age,user.email
                 from user join profile on user.user_id = profile.user_id where user.user_id = %s """
            
            cursorObject.execute(query, (self.user_id,))
            result = cursorObject.fetchone()

            if result:
                print("\n----- PROFILE DETAILS -----")
                print("Firstname:", result[0])
                print("Lastname:", result[1])
                print("DOB:", result[2])
                print("Gender:", result[3])
                print("Phone No:", result[4])
                print("Age:", result[5])
                print("Email:", result[6])
            else:
                 print("Profile not found!")

        except:
            print("Database Error:", e)
        
        finally:
            cursorObject.close()         
                  
    def update(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:
            user_id = int(input("Enter the user_id: "))

            print("1.First name")
            print("2.last name")
            print("3.DOB")
            print("4.Gender")

            choice = int(input("Enter the choice: "))

            if choice==1:
                value = input("Enter the new first name: ")
                query = """Update profile set  firstname = %s where user_id = %s"""

            elif choice ==2:    
                value = input("Enter the new last name: ")
                query = """Update profile set  lasttname = %s where user_id = %s"""

            elif choice ==3:    
                value = input("Enter the new DOB: ")
                query = """Update profile set DOB = %s where user_id = %s"""

            elif choice ==4:    
                value = input("Enter the new gender: ")
                query = """Update profile set gender = %s where user_id = %s"""   

            else:
                 print("Invalid choice")

            cursorObject.execute(query, (value, user_id))
            connection.commit()     
        except:
             print("database error")
        finally:
            cursorObject.close()   

    def delete(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:
            user_id = int(input("Enter the user_id: "))   
            query = """delete from profile where user_id = %s"""
            cursorObject.execute(query, (user_id,))
            connection.commit()
        except:
            print("database error")
        finally:
            cursorObject.close()

class addressdetails:
    def __init__(self, user_id, street_one, street_two,city, state, zipcode, is_default=False):
        self.user_id = user_id
        self.street_one = street_one
        self.street_two = street_two
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.is_default = is_default

class address:

    def add_address(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:
            user_id = int(input("enter user_id: "))
            street = input("enter street-one: ")
            street = input("enter street-two: ")
            city = input("enter city: ")
            state = input("enter state: ")
            zipcode = input("enter zipcode: ")
            is_default = input("is this default address: ") == "yes"

            if is_default:
                cursorObject.execute("update address set is_default = false where user_id = %s", (user_id,))

            cursorObject.execute(
                "insert into address (user_id, street_one,street_two, city, state, zipcode, is_default) values (%s,%s, %s, %s, %s, %s, %s)",
                (user_id, street, city, state, zipcode, is_default))
            connection.commit()
            print("address added successfully!")
        except:
             print("Database error")

        finally:
            cursorObject.close()


    def read_addresses(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor(dictionary=True)

        try:
            user_id = int(input("enter user_id: "))
            
            cursorObject.execute("select * from address where user_id=%s", (user_id,))
            results = cursorObject.fetchall()
        
            if results:
                for i in results:
                    print(f"street_one: {i['street_one']},street_two: {i['street_two']} ,city: {i['city']}, state: {i['state']}, zip: {i['zipcode']}, default: {i['is_default']}")
            else:
                print("no addresses found!")
        except mysql.connector.Error as e:
            print("Database Error:", e)
                     
        finally:
            cursorObject.close()


    def update_address(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:
            addr_id = int(input("enter address id: "))

            print("1. street-1")
            print("2. street-2")
            print("3. city")
            print("4. state")
            print("5. zipcode")
            print("6. set as default")

            choice = int(input("enter your choice: "))

            if choice == 1:
                value = input("enter new street-one: ")
                query = """update address set street_one = %s where id = %s"""

            elif choice == 2:
                value = input("enter new street-two: ")
                query = """update address set street_two = %s where id = %s"""    

            elif choice == 3:
                value = input("enter new city: ")
                query = """update address set city = %s where id = %s"""

            elif choice == 4:
                value = input("enter new state: ")
                query = """update address set state = %s where id = %s"""

            elif choice == 5:
                value = input("enter new zipcode: ")
                query = """update address set zipcode = %s where id = %s"""

            elif choice == 6:
                user_id = int(input("enter user_id: "))
                cursorObject.execute("update address set is_default=false where user_id=%s", (user_id,))
                value = True
                query = """update address set is_default = %s where id = %s"""

            else:
                print("invalid choice")
                return

            cursorObject.execute(query, (value, addr_id))
            connection.commit()
            print("address updated successfully!")

        except:
            print("database error")
        finally:
            cursorObject.close()


    def delete_address(self):
        connection = d1.get_connection()
        cursorObject = connection.cursor()
        try:
            addr_id = int(input("enter address id: "))
            cursorObject.execute("delete from address where id=%s", (addr_id,))
            connection.commit()
            print("address deleted successfully!")
        except:
             print("Datbase error")
        finally:
            cursorObject.close()                     