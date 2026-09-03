from database.dataconnection import databaseconnection

class Categorydetails:
    def __init__(self,cate_name,cate_desc):
        self.cate_name = cate_name
        self.cate_desc = cate_desc

class Category:
    def __init__(self):
        self.connection = databaseconnection()
        cursorObject = self.connection.cursor()
    def create(self):
        
        try:
    
            cate_name = input("Enter category name: ")
            cate_desc = input("Enter the category description: ")
            category = Categorydetails(
                cate_name,
                cate_desc
            )
            query ="""insert into address (cate_name,cate_desc) values (%s,%s)",
                            (cate_name,cate_desc)"""
            self.cursorObject.execute(query,(category))
            self.connection.commit()
            print("address added successfully!")
        except:
            print("Database error")
            
        finally:
            self.cursorObject.close()

    def read(self):

        try:
            cate_id = int(input("Enter the category id: "))
            query = """select * from category where cate_id = %s"""
            self.cursorObject.execute(query)
            result = self.cursorObject.fetchone()
            if result:
                print("\n----Category----")
                print("cate_id:",result[0])
                print("cate_name:",result[1])
                print("cate_desc:",result[2])
            
        except:
            print("Database error")
        finally:
            print("reading category")             

    def update(self):
        try:
            cate_id = int(input("Enter the category-id: "))
        
            print("1.category name")
            print("2.category description")
        
            choice = int(input("Enter the choice: "))
        
            if choice==1:
                value = input("Enter the new category name: ")
                query = """Update categort set cate_name = %s where cate_id = %s"""
        
            elif choice ==2:    
                value = input("Enter the new category description: ")
                query = """Update profile set  lasttname = %s where cate_id = %s"""
            else:
                print("Invalid choice")

            self.cursorObject.execute(query, (value, cate_id))
            self.connection.commit()     
        except:
             print("database error")
        finally:
            print("Updated successfully") 

    def delete(self):   
      
        try:
            cate_id = int(input("Enter the category-id: "))   
            query = """delete from category where cate_id = %s"""
            self.cursorObject.execute(query, (cate_id,))
            self.connection.commit()
        except:
            print("database error")
        finally:
            print("Deletion complete") 
    
            