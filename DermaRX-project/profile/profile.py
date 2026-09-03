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
    def __init__(self):
        db = databaseconnection()
        self.connection = db.get_connection()
        self.cursorObject = self.connection.cursor()

    def create_profile(self):
        try:

            user_id = int(input("Enter the user_id: "))

            query = """select * from user where user_id = %s """
            self.cursorObject.execute(query,(user_id,))
            result = self.cursorObject.fetchone()

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
            self.cursorObject.execute(query,(profile.user_id,profile.firstname,profile.lastname,profile.dob,profile.gender))
            self.connection.commit()
            print("Profile created successfully!")

        except:
            print("Database Error")

        finally:
            print("Created")

    def read(self):
        
        try:
            self.user_id = int(input("Enter the user_id: "))
            query = """select profile.firstname , profile.lastname,profile.dob,profile.gender,user.phoneno,user.age,user.email
                 from user join profile on user.user_id = profile.user_id where user.user_id = %s """
            
            self.cursorObject.execute(query, (self.user_id,))
            result = self.cursorObject.fetchone()

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
            print("Database Error")
        
        finally:
            print("Read")       
                  
    def update(self):
        
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

            self.cursorObject.execute(query, (value, user_id))
            self.connection.commit()     
        except:
             print("database error")
        finally:
            print("Updated") 

    def delete(self):
    
        try:
            user_id = int(input("Enter the user_id: "))   
            query = """delete from profile where user_id = %s"""
            self.cursorObject.execute(query, (user_id,))
            self.connection.commit()
        except:
            print("database error")
        finally:
            print("Deleted")

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

    def __init__(self):
        db = databaseconnection()
        self.connection = db.get_connection()
        self.cursorObject = self.connection.cursor()

    def add_address(self):
        
        try:
            user_id = int(input("enter user_id: "))
            street_one = input("enter street-one: ")
            street_two = input("enter street-two: ")
            city = input("enter city: ")
            state = input("enter state: ")
            zipcode = input("enter zipcode: ")
            is_default = input("is this default address: ") == "yes"

            if is_default:
                self.cursorObject.execute("update address set is_default = false where user_id = %s", (user_id,))

            query = """insert into address(user_id, street_one, street_two, city, state, zipcode, is_default)
                values (%s, %s, %s, %s, %s, %s, %s)"""
            values = (
                user_id,
                street_one,
                street_two,
                city,
                state,
                zipcode,
                is_default
            )

            self.cursorObject.execute(query,values)
            self.connection.commit()
            print("address added successfully!")
        except:
             print("Database error")

        finally:
           print("Added ")


    def read_addresses(self):

        try:
            user_id = int(input("enter user_id: "))
            
            query = """select * from address where user_id=%s"""
            self.cursorObject.execute(query,(user_id,))
            results = self.cursorObject.fetchall()
        
            if results:
                for i in results:
                    print("street_one:", i[2])
                    print("street_two:",i[7])
                    print("city:",i[3]) 
                    print("state:",i[4])
                    print("zip:",i[5])
                    print("default:",i[6])
            else:
                print("no addresses found!")
        except Exception as e:
            print("Database Error:",e)
                     
        finally:
            print("Read")


    def update_address(self):
 
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
                self.cursorObject.execute("update address set is_default=false where user_id=%s", (user_id,))
                value = True
                query = """update address set is_default = %s where id = %s"""

            else:
                print("invalid choice")
                return

            self.cursorObject.execute(query, (value, addr_id))
            self.connection.commit()
            print("address updated successfully!")

        except:
            print("database error")
        finally:
            print("updated ")

    def delete_address(self):
       
        try:
            addr_id = int(input("enter address id: "))
            self.cursorObject.execute("delete from address where id=%s", (addr_id,))
            self.connection.commit()
            print("address deleted successfully!")
        except:
             print("Datbase error")
        finally:
            print("Deleted")                   