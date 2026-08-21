# works on lifo
# bottom is 0 and top is n-1
# if stack is empty its  top /pointer /counter is -1 
# it will work till the pop 
# **PEAK** -->>> TOP element of the stack

# class Stack:

#     def __init__(self,capacity):
#         self.arr = [0]*capacity 
#         self.top = -1
#         self.capacity = capacity

#     def push(self,number):
#         if self.top >= self.capacity:
#             print("Stack is full.Can't add more")
#             return

#         self.top += 1
#         self.arr[self.top] = number

#     def peek(self):
#         print("The peek element is:",self.arr[self.top])

#     def pop(self):  #whenever we want to pop element we will call this

#         if self.top < 0:
#             print("Stack is empty. Can't pop more elements!!!!")
#             return
        
#         item = self.arr[self.top]
#         self.arr[self.top] = '#'
#         print("Popped element is:",item)
#         self.top -=1
#     def isempty(self):
#         if self.top ==-1:
#             print("stack is empty")
#         else:
#             print("stack is not empty")    


#     def iterate(self):
#         for i in range(self.top,-1,-1):
#             print("stack element is:",self.arr[i])


# s1 = Stack(6)
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# s1.push(5)
# s1.push(6)
# s1.iterate()
# s1.peek()

# s1.isempty()
# s1.pop()
# s1.pop()
# s1.pop()
# # s1.pop()
# # s1.pop()
# # s1.pop()
# # s1.pop()
# s1.peek()
# s1.iterate()



# Program 4:Implement Two Stacks Using One Array
# class Stack:

#     def __init__(self,capacity):
#         self.arr = [0]*capacity 
#         self.top = -1
#         self.capacity = capacity

#     def push(self,number):
#         if self.top >= self.capacity:
#             print("Stack is full.Can't add more")
#             return
#         self.top += 1
#         self.arr[self.top] = number   

#     def twostack(self):
#         if self.top%2==0:
#             for i in range(0,self.top//2):
#                 print("stack1 element is:",self.arr[i])
#             for i in range(self.top//2,self.top+1):
#                 print("stack2 element is:",self.arr[i])     
#         else:
#             for i in range(0,self.top//2+1):
#                 print("stack1 element is:",self.arr[i])
#             for i in range(self.top//2,self.top+1):
#                 print("stack2 element is:",self.arr[i])  

# s1 = Stack(5)
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# s1.push(5)        
# s1.twostack()      


# class Infixtopostfix:

#     def __init__(self,string):
#         self.string = string

#     def get_precedence(self,ch):

#         precedence = 0
#         if (ch == '*'or ch=='/'):
#             precedence = 2
#         else:
#             precedence = 1

#         return precedence        

#     def infix_to_postfix(self):

#         result = ''  
#         list1 = []
#         for i in range(len(self.string)):
#             ch = self.string[i]

#             if (ch >='a' and ch <='z') or (ch >= 'A' and ch <='Z') or (ch >= '0' and ch <= '9'):
#                 result += ch

#             elif (ch=='+' or ch=='-' or ch=='*' or ch =='/'):

#                 if len(list1)!=0 and self.get_precedence(ch) > self.get_precedence(list1[-1]):
#                     list1.append(ch)

#                 elif len(list1)!=0 and self.get_precedence(ch) <= self.get_precedence(list1[-1]):
#                     while len(list1) != 0 and self.get_precedence(ch) <= self.get_precedence(list1[-1]):
#                         result += list1.pop()    
#                     list1.append(ch)

#                 else:
#                     list1.append(ch)

#             else:
#                 print("invalid string")

#         while len(list1) != 0:
#             result += list1.pop() 
#         print(result)        


# string = input("Enter the string: ")
# ip = Infixtopostfix(string)     
# ip.infix_to_postfix()




# class Infixtopostfix:

#     def __init__(self,string):
#         self.string = string

#     def get_precedence(self,ch):

#         precedence = 0
#         if (ch == '*'or ch=='/'):
#             precedence = 2
#         else:
#             precedence = 1

#         return precedence        

#     def infix_to_postfix(self):

#         result = ''  
#         list1 = []
#         for i in range(len(self.string)):
#             ch = self.string[i]

#             if (ch >='a' and ch <='z') or (ch >= 'A' and ch <='Z') or (ch >= '0' and ch <= '9'):
#                 result += ch

#             elif ch=='(':
#                 list1.append(ch)

#             elif ch==')':
#                 while list1[-1] !='(':
#                     result += list1.pop()
#                 list1.pop()
                
#             elif (ch=='+' or ch=='-' or ch=='*' or ch =='/'):

#                 if len(list1)!=0 and list1[-1] !='(' and self.get_precedence(ch) > self.get_precedence(list1[-1]):
#                     list1.append(ch)

#                 elif len(list1)!=0 and list1[-1] !='(' and self.get_precedence(ch) <= self.get_precedence(list1[-1]):
#                     while len(list1) != 0 and list1[-1] !='(' and self.get_precedence(ch) <= self.get_precedence(list1[-1]):
#                         result += list1.pop()    
#                     list1.append(ch)

#                 else:
#                     list1.append(ch)

#             else:
#                 print("invalid string")

#         while len(list1) != 0:
#             result += list1.pop() 
#         print(result)        


# string = input("Enter the string: ")
# ip = Infixtopostfix(string)     
# ip.infix_to_postfix()



# # infix to prefix:
# class Infixtoprefix:

#     def __init__(self,string):
#         self.string = string

#     def get_precedence(self,ch):

#         precedence = 0
#         if (ch == '*'or ch=='/'):
#             precedence = 2
#         else:
#             precedence = 1

#         return precedence        

#     def infix_to_prefix(self):

#         result = ''  
#         list1 = []
#         self.string = self.string[::-1]
#         for i in range(len(self.string)):
#             ch = self.string[i]

#             if (ch >='a' and ch <='z') or (ch >= 'A' and ch <='Z') or (ch >= '0' and ch <= '9'):
#                 result += ch

#             elif ch==')':
#                 list1.append(ch)

#             elif ch=='(':
#                 while list1[-1] !=')':
#                     result += list1.pop()
#                 list1.pop()
                
#             elif (ch=='+' or ch=='-' or ch=='*' or ch =='/'):

#                 if len(list1)!=0 and list1[-1] !=')' and self.get_precedence(ch) < self.get_precedence(list1[-1]):
#                     list1.append(ch)

#                 elif len(list1)!=0 and list1[-1] !=')' and self.get_precedence(ch) >= self.get_precedence(list1[-1]):
#                     while len(list1) != 0 and list1[-1] !=')' and self.get_precedence(ch) >= self.get_precedence(list1[-1]):
#                         result += list1.pop()    
#                     list1.append(ch)

#                 else:
#                     list1.append(ch)

#             else:
#                 print("invalid string")

#         while len(list1) != 0:
#             result += list1.pop() 
#         print(result[::-1])   


# string = input("Enter the string: ")
# ip = Infixtoprefix(string)     
# ip.infix_to_prefix()




# postfixtoinfix
# class PostfixToInfix:
#     def __init__(self, string):
#         self.string = string

#     def postfix_to_infix(self):
#         list1 = []
        
#         for i in range(len(self.string)):
#             ch = self.string[i]

#             if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9'):
#                 list1.append(ch)     
           
#             elif ch in ['+', '-', '*', '/']:
#                 if len(list1) < 2:
#                     print("Invalid string")
#                     return
                
#                 first = list1.pop()   
#                 second = list1.pop()

#                 result = "("+second+ch+first+")"
#                 list1.append(result)
#             else:
#                 print("Invalid string")    
#                 return
     
#         if len(list1) == 1:
#             print(list1[0])
#         else:
#             print("Invalid string")

# string = input("Enter the string: ")
# ip = PostfixToInfix(string)     
# ip.postfix_to_infix()


# prefix to infix:
# class prefixtoInfix:

#     def __init__(self,string):
#         self.string = string
     

#     def prefix_to_infix(self):

#         result = ''  
#         list1 = []
#         self.string = self.string[::-1]
#         for i in range(len(self.string)):
#             ch = self.string[i]

#             if (ch >='a' and ch <='z') or (ch >= 'A' and ch <='Z') or (ch >= '0' and ch <= '9'):
#                 list1.append(ch)     
#             elif (ch=='+' or ch=='-' or ch=='*' or ch =='/'):
#                 if len(list1) < 2:
#                     print("Invalid string")
#                     return

#                 first = list1.pop()
#                 second = list1.pop()

#                 result = f"({first}{ch}{second})"
#                 list1.append(result)
#             else:
#                 print("Invalid string")    
            
#         if len(list1)==1:
#             print(list1[0])

# string = input("Enter the string: ")
# ip = prefixtoInfix(string)     
# ip.prefix_to_infix()




# prefixtopostfix
# class prefixtopostfix:
#     def __init__(self, string):
#         self.string = string

#     def prefix_to_postfix(self):
#         list1 = []
#         self.string = self.string[::-1]
        
#         for i in range(len(self.string)):
#             ch = self.string[i]

#             if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9'):
#                 list1.append(ch)     
           
#             elif ch in ['+', '-', '*', '/']:
#                 if len(list1) < 2:
#                     print("Invalid string")
#                     return
                
#                 first = list1.pop()   
#                 second = list1.pop()

#                 result = f"{first}{second}{ch}"
#                 list1.append(result)
#             else:
#                 print("Invalid string")    
#                 return
     
#         if len(list1) == 1:
            
#             print(list1[-1])
#         else:
#             print("Invalid string")

# string = input("Enter the string: ")
# ip = prefixtopostfix(string)     
# ip.prefix_to_postfix()




# postfixevaluation
# class PostfixToInfix:
#     def __init__(self, string):
#         self.string = string

#     def postfix_to_infix(self):
#         list1 = []
        
#         for i in range(len(self.string)):
#             ch = self.string[i]

#             if (ch >='0' and ch <='9') :
#                 list1.append(ch)
#             else:
#                 first=list1.pop()
#                 second=list1.pop()    
#                 if ch== '+':
#                     result = int(second) + int(first)
#                     list1.append(result)
#                 elif ch== '-':
#                     result = int(second) - int(first)
#                     list1.append(result)   
#                 elif ch== '*':
#                     result = int(second) * int(first)
#                     list1.append(result)  
#                 elif ch=='/':
#                     result = int(second) / int(first)
#                     list1.append(result)     
#                 else:
#                     print("invalid charcter")      
            
#         if len(list1) == 1:
#             print(list1[0])
#         else:
#             print("Invalid string")

# string = input("Enter the string: ")
# ip = PostfixToInfix(string)     
# ip.postfix_to_infix()


# *******RECURSION******
def functionA(n):
    print("Inside function A!!!!")
    if n%2==0:
        print(a,"is even.")
    else:
        print(a,"is odd.")    

a = 5
b = 10
#a value to copy /// there is no realtion between a and n /// if a get change n will not get change and  vice versa 
functionA(a)
a = 12
functionA(a)
