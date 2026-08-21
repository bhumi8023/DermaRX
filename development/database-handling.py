import mysql.connector

try:

    connection = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'entangle')
    print("Connection to db is:",connection)

    cursorObject = connection.cursor()
    query = "select * from Book"
    cursorObject.execute(query)
    result = cursorObject.fetchall()

    for x in result:
        print(x)

    
    # cursorObject.execute("ALTER TABLE book ADD published_year INT")
      
    # query = """insert into book(title,author,price) values(%s,%s,%s)"""
    # values = ("C++ Learning","qwerty",444)
    # cursorObject.execute(query,values)
    # print("Rows inserted")
    # connection.commit()  
    cursorObject.execute("DESCRIBE book")
    
    table_structure = cursorObject.fetchall()
    for column in table_structure:
        print(column)
 


except IOError:
    print("Can't connect to database")

finally:
    print("Closing connection")
    connection.close
    