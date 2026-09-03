from database.dataconnection import databaseconnection
from profile.profile import Profile,address
from user.userregistration import UserRegistration
from catelog.category import Category,Product


def main_menu():
  
    print("\n***** DERMA-RX *****")
    print("1. user (register/login)")
    print("2. profile")
    print("3. address")
    print("4. category")
    print("5. product")
    

    choice = input("\nenter your choice: ")

    if choice == "1":
        UserRegistration().menu()
    elif choice == "2":
        Profile().menu()
    elif choice == "3":
        address().menu()
    elif choice == "4":
        Category().menu()
    elif choice=="5":
        Product().menu()    
    else:
        print("invalid choice")

if __name__ == "__main__":
    main_menu()
