from database.dataconnection import databaseconnection

class Categorydetails:
    def __init__(self,cate_name,cate_desc):
        self.cate_name = cate_name
        self.cate_desc = cate_desc

class Category:
    def __init__(self):
        db = databaseconnection()
        self.connection = db.get_connection()
        self.cursorObject = self.connection.cursor()

    def menu(self):
       
        print("\n--- category menu ---")
        print("1. create category")
        print("2. read category")
        print("3. update category")
        print("4. delete category")
            

        choice = input("enter your choice: ")

        if choice == "1":
            self.create()
        elif choice == "2":
            self.read()
        elif choice == "3":
            self.update()
        elif choice == "4":
            self.delete()
            
        else:
            print("invalid choice, please try again.")
    
    def create(self):
        
        try:
    
            cate_name = input("Enter category name: ")
            cate_desc = input("Enter the category description: ")
            category = Categorydetails(
                cate_name,
                cate_desc
            )
            query ="""insert into category (cate_name,cate_desc) values (%s,%s)"""
            self.cursorObject.execute(query,(cate_name,cate_desc))
            self.connection.commit()
            print("address added successfully!")
        except Exception as e:
            print("Database error:", e)
            
        finally:
            self.cursorObject.close()

    def read(self):

        try:
            cate_id = int(input("Enter the category id: "))
            query = """select * from category where cate_id = %s"""
            self.cursorObject.execute(query,(cate_id,))
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
                query = """Update category set cate_name = %s where cate_id = %s"""
        
            elif choice ==2:    
                value = input("Enter the new category description: ")
                query = """Update category set  cate_desc = %s where cate_id = %s"""
            else:
                print("Invalid choice")
                return

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
    
class Productdetails:

    def __init__(self,cate_id,prod_name,prod_desc,price,slug):
        self.cate_id = cate_id
        self.prod_name = prod_name
        self.prod_desc = prod_desc
        self.price = price
        self.slug = slug

class Product:

    def __init__(self):
        db = databaseconnection()
        self.connection = db.get_connection()
        self.cursorObject = self.connection.cursor()
    

    def menu(self):
            
        print("----Product Menu----")
        print("1. create product")
        print("2. read product")
        print("3. update product")
        print("4. delete product")
            
    
        choice = input("enter your choice: ")
    
        if choice == "1":
            self.create()
        elif choice == "2":
            self.read()
        elif choice == "3":
            self.update()
        elif choice == "4":
            self.delete()
        else:
            print("invalid choice, please try again.")

    def create(self):

        try:
            cate_id = int(input("Enter the category-id: "))
            prod_name = input("Enter the product name: ")
            prod_desc = input("Enter the product description: ")
            price = float(input("Enter the price of the product: "))
            slug = input("Enter the slug: ")

            values = (
                    cate_id,
                    prod_name,
                    prod_desc,
                    price,
                    slug )
            query = """insert into product(cate_id,prod_name,prod_desc,price,slug)values
                (%s,%s,%s,%s,%s)"""
            self.cursorObject.execute(query,values)
            self.connection.commit()
           
            
        except Exception as e:         
            print("Database error: ",e)    

        finally:
            print("product added successfully")

    def read(self):

        try:

            cate_id = int(input("Enter the category id: "))
            query = """select * from product where cate_id = %s"""
            self.cursorObject.execute(query,(cate_id,))
            result = self.cursorObject.fetchall()
            self.cursorObject.fetchall()
            if result:
                for i in result:  
              
                    print("Product ID:", i[0])
                    print("Category ID:", i[1])
                    print("Product Name:", i[2])
                    print("Description:", i[3])
                    print("Price:", i[4])
                    print("Slug:",i[5])
                    print("---------------------------")

        except Exception as e:
            print("databse error:",e)    
        finally:
            print("All product displayed")  

    def update(self):  
      
        try:
            prod_id = int(input("enter the product id to update: "))
            print("choose what you want to update:")
            print("1. product name")
            print("2. product description")
            print("3. price")
            print("4. slug")

            choice = int(input("enter your choice (1-4): "))

            if choice == 1:
                new_value = input("enter new product name: ")
                query = """update product set prod_name = %s where product_id = %s"""
            elif choice == 2:
                new_value = input("enter new product description: ")
                query = """update product set prod_desc = %s where product_id = %s"""
            elif choice == 3:
                new_value = float(input("enter new price: "))
                query = """update product set price = %s where product_id = %s"""
            elif choice == 4:
                new_value = input("enter new slug: ")
                query = """update product set slug = %s where product_id = %s"""
            else:
                print("invalid choice")
                return

            values = (new_value, prod_id)
            self.cursorobject.execute(query, values)
            self.connection.commit()
           

        except Exception as e:
            print("database error:", e)
        finally:
            print("product updated successfully!")


    def delete(self):
        try:
            product_id = int(input("enter the product id to delete: "))
            query = """delete from product where product_id = %s"""
            self.cursorObject.execute(query, (product_id,))
            self.connection.commit()
            print("product deleted successfully!")

        except Exception as e:
            print("database error:", e)
        finally:
            print("deletion done")    
































































































































































































































































































































































































































































