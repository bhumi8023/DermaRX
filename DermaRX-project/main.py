from database.dataconnection import databaseconnection
from profile.profile import Profile,address
from user.userregistration import UserRegistration
from catelog.category import Category

ur1 = UserRegistration()
p1 = Profile()
a1 = address()
c1 = Category()

print("\n*****DERMA-RX******")
print("1. Register/login")
print("2. Profile")
print("3. Address")
print("4. Category")
choice = input("\nEnter your choice: ")
if choice == "1":
    print("1. Register")
    print("2. Login")
    choice = input("\nEnter your choice: ")
    if choice =="1":
        ur1.register()
    elif choice == "2":
        ur1.login() 
    else:
     print("Wrong choice")
elif choice=="2":
    print("\n*****DERMA-RX-Profile******")
    print("1.Create")
    print("2.Read")
    print("3.Update")
    print("4.Delete")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        p1.create_profile()
    elif choice == "2":
        p1.read()
    elif choice=="3":
        p1.update()
    elif choice == "4":
        p1.delete() 
    else:
        print("Wrong choice") 

elif choice =="3":
    
    print("1.add address")
    print("2.view addresses")
    print("3.update address")
    print("4.delete address")
    choice = input("\nenter your choice: ")

    if choice == "1":
        a1.add_address()
    elif choice == "2":
        a1.read_addresses()
    elif choice == "3":
        a1.update_address()
    elif choice == "4":
        a1.delete_address()
    else:
        print("wrong choice")
        
elif choice=="4":
    print("1.add category")
    print("2.view category")
    print("3.update category")
    print("4.delete category")
    choice = input("\nenter your choice: ")
    if choice == "1":
        c1.create()
    elif choice == "2":
        c1.read()
    elif choice == "3":
        c1.update()
    elif choice == "4":
        c1.delete()
    else:
        print("wrong choice")
else:
    print("invalid choice")







        






  
