from datetime import date
import mysql.connector


class System:

    def __init__(self):
        self.connection = mysql.connector.connect(user = 'root',password = 'root',host = 'localhost',database = 'entangle')
        print("Connection to db is:",self.connection)
        
        cursorObject = self.connection.cursor()
        cursorObject.execute("""
                CREATE TABLE IF NOT EXISTS Student1 (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) ,
                email VARCHAR(255) ,
                age INT 
                )
            """)
        
        cursorObject.execute("""
                CREATE TABLE IF NOT EXISTS  Course (
                course_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) ,
                duration VARCHAR(255) ,
                fees decimal(10,2) 
                )
            """)
        
        cursorObject.execute("""
                CREATE TABLE IF NOT EXISTS  Enrollment (
                student_id INT,
                course_id INT,
                enrollment_date DATE ,
                FOREIGN KEY (student_id) REFERENCES Student1(student_id),
                FOREIGN KEY (course_id) REFERENCES Course(course_id) 
                )
            """)    
        self.connection.commit()
        cursorObject.close()
    def get_connection(self):
        return self.connection
        

s1 =  System()


class Student:
    def __init__(self,id=None,name=None,email=None,age=None):
        self.id = id 
        self.name = name
        self.email = email
        self.age = age 

    def add(self):
        
        connection = s1.get_connection()
        cursorObject = connection.cursor()
        try:
            query = "INSERT INTO Student1 (name, email, age) VALUES (%s, %s, %s)"
            cursorObject.execute(query, (self.name, self.email, self.age))
            connection.commit()   
            cursorObject.execute("SELECT * FROM Student1")
            result = cursorObject.fetchall()
            
            for x in result:
                print(x)

        except:
            print("Something wrong")

        finally:
            print("Insertion complete")
            cursorObject.close()
           

    def view_all_student(self):
        connection = s1.get_connection()
        cursorObject = connection.cursor()
        try:
           
            cursorObject.execute("SELECT * FROM Student1")
            record = cursorObject.fetchall()
            if not record:
                print("No student records found.")
                return
            for x in record:
                print(x)
        except:
            print("Can't fetch Student")

        finally:
            # print("")  
            cursorObject.close()

      
    def find_student(self):

        try:
            student_id = int(input("Enter the student id: "))
            connection = s1.get_connection()
            cursorObject = connection.cursor()
            cursorObject.execute("SELECT * FROM Student1 WHERE student_id = %s", (student_id,))
            row = cursorObject.fetchone()
            if row:
                print(f"Student found",row)
            else:
                print("Student not found")
        except:
            print("Inavlid id")

        finally:
            cursorObject.close()

    def update_student(self):
        try:
            student_id = int(input("Enter the student id: "))
            connection = s1.get_connection()
            cursorObject = connection.cursor()
            cursorObject.execute("SELECT * FROM Student1 WHERE student_id = %s", (student_id,))
            if  not cursorObject.fetchone():
                print("Student not found")

            new_name = input("Enter New Name: ")
            new_email = input("Enter New Email: ")
            new_age = int(input("Enter New Age: "))
            
            cursorObject.execute(
                "UPDATE student SET name = %s, email = %s, age = %s WHERE id = %s",
                (new_name, new_email, new_age,id)
            )
            connection.commit()
            
        except:
            print("Inavlid id")
        
        finally:
            cursorObject.close()

    def delete_student(self):
        try:
            student_id = int(input("Enter the student id: "))
            connection = s1.get_connection()
            cursorObject = connection.cursor()
            cursorObject.execute("DELETE FROM Student1 WHERE student_id = %s", (student_id,))

        except:
            print("Inavlid id")
                
        finally:
            cursorObject.close()

class Courses:
    def __init__(self):
        pass

    def add_course(self):

        connection = s1.get_connection()
        cursorObject = connection.cursor()
        name = input("Enter Course Name: ")
        duration = input("Enter Duration: ")
        try:
            fees = float(input("Enter Course Fees: "))
            
            connection = s1.get_connection()
            cursorObject = connection.cursor()
            cursorObject.execute(
                "INSERT INTO Course (name, duration, fees) VALUES (%s, %s, %s)",
                (name, duration, fees)
            )
            connection.commit()
        except:
            print("errorrrrr")
        finally:
            print("Added successfully")
            cursorObject.close()

    def  view_courses(self):
        try:
            connection = s1.get_connection()
            cursorObject = connection.cursor()
            cursorObject.execute("SELECT * FROM Course")
            result = cursorObject.fetchall()

            for course_id, name, duration, fees in result:
                print(f"ID: {course_id} | Name: {name} | Duration: {duration} | Fees: {float(fees)}")
        except:
            print("Error finding in course" ) 

        finally:
            print("all courses ")      
            cursorObject.close()     

    def enroll_student(self):

        try:
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            
            connection = s1.get_connection()
            cursorObject = connection.cursor()
            
            cursorObject.execute(
                "INSERT INTO Enrollment (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)",
                (student_id, course_id, date.today())
            )
            
            connection.commit()
        except:
            print("inavalid course id or student id")

        finally:
            print("course added")
            cursorObject.close() 

    def view_studentcourses(self):
        try:
            connection = s1.get_connection()
            cursorObject = connection.cursor()
            cursorObject.execute("SELECT * FROM Enrollment")
            result = cursorObject.fetchall()
        
            for student_id, course_id, enroll_date in result:
                print(f"Student ID: {student_id} | Course ID: {course_id} | Enrolled Date: {enroll_date}")
        except:
            print("Error finding in course" ) 
        
        finally:
            print("all courses ")      
            cursorObject.close()   

    def run_exit(self):
        choice = input("Enter choice (1-10): ")
 
        if choice == '1': st1.add()
        elif choice == '2': st1.view_all_student()
        elif choice == '3': st1.find_student()
        elif choice == '4': st1.update_student()
        elif choice == '5': st1.delete_student()
        elif choice == '6': self.add_course()
        elif choice == '7': self.view_courses()
        elif choice == '8': self.enroll_student()
        elif choice == '9': self.view_studentcourses()
        elif choice == '10': print("Byeeebyeeee")
        else:
            print("Inavlid choice")

           


st1 = Student(name= 'bhoomika',email='bhumi123.com',age=21)
co1 = Courses()
co1.run_exit()

