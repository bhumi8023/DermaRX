# def palindrome(user_input:str):
#     left = 0
#     right = len(user_input) - 1

#     while left < right:
#         if user_input[left] != user_input[right]:
#             return False
#         left += 1
#         right -= 1

#     return True

# user_input = input("Enter the string: ")
# if palindrome(user_input):
#     print("It is palindrome")
# else:
#     print("It is not palindrome")    


# 1. count dispaly
# class Display:
#     def __init__(self,text):
#         self.text = text
#     def calculation(self):
#         length = 0
#         for i in self.text:
#                 length += 1
#         print(length)    
# d1 =Display('brhfrjsoi')
# d1.calculation()


# # 3,4   Count vowel ,Consonants in String 
# class Display:
#     def __init__(self,text):
#         self.text = text
   
#     def vowles(self):
#       count = 0
#       constant_count = 0
#       for i in self.text:
#           if i == 'a' or i=='i'or i=='u' or i=='e' or i == 'o' or i =='A' or i == 'E' or i== 'I' or i =='O' or i== 'U':
#               count += 1
#           else:
#               constant_count += 1    
#       print("The vowel count: ", count)
#       print("The constant count: ",constant_count)        
# d1=Display('bhomikalhriowsn')
# d1.vowles()


# Program 5: Count Spaces in String 
# class Display:
#     def __init__(self,text):
#         self.text = text
#     def calculation(self):

#         count = 0
#         for i in self.text:
#             if i == ' ':
#                 count += 1
#         print(count)
# d1 = Display('jrnd dejkf eredd f4res f4rfe')
# d1.calculation()     


# Program 6: Count Digits in String and  Count Alphabets in String
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def calculaton(self):
#         count = 0
#         number_count = 0
#         for i in self.text:
#             if  48 <= ord(i) <= 57:
#                 number_count += 1
#             else:
#                 count += 1    
#         print("The number count is: ",number_count)
#         print("The alphabet count: ",count)

# text = input("Enter the string:")
# d1 = Display(text)
# d1.calculaton()     


#Program 8: Count Special Characters 
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def calcultaion(self):
#         count = 0
#         for i in self.text:
#             if not (48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i)<= 122):
#                 count += 1
#         print(count)

# text = input("Enter the string:")
# d1 = Display(text)
# d1.calcultaion()





# Program 9: Count Uppercase Letters
# class Display:
#     def __init__(self,text):
#         self.text = text
#     def calcultaion(self):
#         count = 0
#         for i in self.text: 
#             if 65 <= ord(i) <= 90:
#                 count += 1
#         print(count)
# text = input("Enter the string:")
# d1 = Display(text)
# d1.calcultaion()




# Program 10: Count Lowercase Letters
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def calculate(self):
#         count = 0
#         for i in self.text:
#             if 97 <= ord(i) <= 122:
#                 count += 1
#         print(count)


# text = input("Enter the string:")
# d1 = Display(text)
# d1.calculate()




# Program 11: Count Words in String 
# class Text:

#     def __init__(self,string):
#         self.string = string
#         count = self.string.split()
#         print(len(count))


#     # def count(self):
#     #     is_word = False
#     #     count = 0
#     #     for i in self.string:
#     #         if i !=' ' :
#     #             if not is_word:
#     #                 count += 1
#     #                 is_word = True
#     #         else:
#     #             is_word= False    

#     #     print(count)        

# string = input("Enter the string: ")    
# t1 =Text(string)
# # t1.count()



# Program 12: Display String Character by Character
# class Display:
#     def __init__(self,text):
#         self.text = text

#         for i in text:
#             print(i)


# text = input("Enter the string:")
# d1 = Display(text)




# Program 13: Display String in Reverse Order

# class Display:
#     def __init__(self,text):
#         self.text = text
#         print(str(self.text[::-1]))


# text = input("Enter the string:")
# d1 = Display(text)




# Program 14: Find First Character  Program 15: Find Last Character

# class Display:
#     def __init__(self,text):
#         self.text = text

#         print("The first letter is:",text[0])
#         print("The last letter is:",text[-1])

# text = input("Enter the string: ")
# d1 = Display(text)



# Program 16: Convert to Uppercase 
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def uppercase(self):
#         upper = self.text.upper()
#         print(upper)

# text = input("Enter the string: ")
# d1 = Display(text)
# d1.uppercase()



# Program 17: Convert to Lowercase
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def lowercase(self):
#         lower = self.text.lower()
#         print(lower)

# text = input("Enter the string: ")
# d1 = Display(text)
# d1.lowercase()



# Program 18: Toggle Case
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def toggle(self):
#         print(self.text.swapcase())

# text = input("Enter the string: ")
# d1 = Display(text)
# d1.toggle()




# Program 19: Capitalize First Letter of String
# class Display:
#     def __init__(self,text):
#         self.text = text
#         print(self.text.capitalize())       

# text = input("Enter the string: ")
# d1 = Display(text)


# Program 20: Capitalize First Letter of Each Word 

# class Display:
#     def __init__(self,text):
#         self.text = text

#         print(self.text.title()) 

# text = input("Enter the string: ")
# d1 = Display(text)





# Program 21: Replace All Spaces with Underscore 
# class Display:
#     def __init__(self,text):
#         self.text = text
#         print(self.text.replace(" ","_"))


# text = input("Enter the string: ")         
# d1 = Display(text)               






# Program 22: Replace Character X with Y
# class Display:
#     def __init__(self,text,X,Y):
#         self.text = text
#         self.X = X
#         self.Y = Y
#     def replace(self):
#         result = ""
#         for i in self.text:
#             if i == self.X:
#                 result += self.Y
#             else:
#                 result += i 
#         print(result)

# text = input("Enter the string: ")
# X = input("Enter the X: ")
# Y = input("Enter the Y: ")
# d1 =Display(text,X,Y)
# d1.replace()




# Program 23: Remove All Spaces
# class Display:
#     def __init__(self,text):
#         self.text = text
#         print(self.text.replace(" ",""))

# text = input("Enter the string: ")
# d1 = Display(text)



# Program 24: Remove Leading Spaces 
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):
        # print(self.text.lstrip())


# text = input("Enter the string: ")
# d1 = Display(text)
# d1.remove()



# Program 25: Remove Trailing Spaces
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):
#         print(self.text.rstrip())


# text = input("Enter the string: ")
# d1 = Display(text)
# d1.remove()


# Program 26: Remove Extra Spaces (Keep Single) 
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):
#         words = self.text.split()
#         print(" ".join(words))


# text = input("Enter the string: ")
# d1 = Display(text)
# d1.remove()



# Program 27: Count Occurrence of Character 
# class Display:
#     def __init__(self,text,X):
#         self.text = text
#         self.X =X
#     def count(self):
#         count = 0
#         for i in self.text:
#             if i == self.X:
#                 count += 1    
#         print("The count of ",self.X,"is:",count)  
# text = input("Enter the string: ")
# X= input("The Charcter is :")
# d1 = Display(text,X)
# d1.count()              




# Program 28: Find First Occurrence of Character
# class Display:
#     def __init__(self,text,X):
#         self.text = text
#         self.X =X
#     def count(self):
#         for i in range(len(self.text)):
#             if self.text[i] == self.X:
#                 print("The position of",self.X,"is:",i)  
#                 return
            
#         print(-1)    

# text = input("Enter the string: ")
# X= input("The Charcter is: ")
# d1 = Display(text,X)
# d1.count()              




# Program 29: Find Last Occurrence of Characte
# class Display:
#     def __init__(self,text,X):
#         self.text = text
#         self.X =X
#     def count(self):
#        position = self.text.rfind(self.X)
#        print(position)
            
#        print(-1)    

# text = input("Enter the string: ")
# X= input("The Charcter is: ")
# d1 = Display(text,X)
# d1.count()              



# Program 30: Find All Positions of Character
# class Display:
#     def __init__(self,text):
#         self.text = text
       
#     def count(self):
#         for i in range(len(self.text)):
#             print("The position of",self.text[i],"is:",i)  
       

# text = input("Enter the string: ")

# d1 = Display(text)
# d1.count()    

# Program 31: Remove All Occurrences of Character
# class Display:
#     def __init__(self,text,X):
#         self.text = text
#         self.X =X
       
#     def count(self):
#         print(self.text.replace(self.X,""))

# text = input("Enter the string: ")
# X = input("Enter the character: ")
# d1 = Display(text,X)
# d1.count()    




# Program 32: Remove Digits from String 
# class Display:
#     def __init__(self,text):
#         self.text = text
     
       
#     def count(self):
#         text2 =""
#         for i in range(len(self.text)):
#             if 48 <= ord(self.text[i]) <= 57:
#                 pass
#             else:
#                 text2 += self.text[i]
#         print(text2)        
       
# text = input("Enter the string: ")
# d1 = Display(text)
# d1.count()    




# Program 33: Remove Special Characters 
# class Display:
#     def __init__(self,text):
#         self.text = text
     
       
#     def count(self):
#         text2 =""
#         for i in range(len(self.text)):
#             if self.text[i].isalnum() or self.text[i] == ' ':
#                 text2 += self.text[i]
#         print(text2)   
       
# text = input("Enter the string: ")
# d1 = Display(text)
# d1.count()    





# Program 34: Check if Palindrome

# class Display:
#     def __init__(self,text):
#         self.text = text

#     def palindrome(self):
#         if self.text == self.text[::-1]:
#             print("Yes")
#         else:
#             print("No")    


# text = input("Enter the string: ")
# d1 = Display(text)
# d1.palindrome()





# Program 35: Check if Two Strings are Equal 
# class Display:
#     def __init__(self,text1,text2):
#         self.text1 = text1
#         self.text2 = text2

#     def equal(self):
#         if self.text1 == self.text2:
#             print("Yes,it's equal")
#         else:
#             print("No,it's not equal")    


# text1 = input("Enter the string1: ")
# text2 = input("Enter the string2: ")
# d1 = Display(text1,text2)
# d1.equal()





# Program 36: Check if Two Strings are Equal (Ignore Case) 
# class Display:
#     def __init__(self,text1,text2):
#         self.text1 = text1
#         self.text2 = text2

#     def equal(self):
#         if self.text1.lower() == self.text2.lower():
#             print("Yes,it's equal")
#         else:
#             print("No,it's not equal")    


# text1 = input("Enter the string1: ")
# text2 = input("Enter the string2: ")
# d1 = Display(text1,text2)
# d1.equal()





# Program 37: Compare Two Strings Lexicographically
# class Display:
#     def __init__(self,text1,text2):
#         self.text1 = text1
#         self.text2 = text2

#     def equal(self):
#         # self.text1 = self.text1.lower()
#         # self.text2 = self.text2.lower()
#         if self.text1 < self.text2:
#             print(self.text1,"comes first")
#         elif self.text1 > self.text2:
#             print(self.text2,"comes first")    
#         else:
#             print("Both equal")    


# text1 = input("Enter the string1: ")
# text2 = input("Enter the string2: ")
# d1 = Display(text1,text2)
# d1.equal()






# Program 38: Check if String Contains Only Alphabets 
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         if self.text1.isalpha():
#             print("The string contain alphabets only")
#         else:
#             print("The string does not contain only alphabets")    


# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()





# Program 39: Check if String Contains Only Digits 
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         if self.text1.isnumeric():
#             print("The string contain numbers only")
#         else:
#             print("The string does not contain only numbers")    


# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()



# Program 40: Check if String is Alphanumeric
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         if self.text1.isalnum():
#             print("The string contain alphabets and numbers only")
#         else:
#             print("The string does not contain only alphabets and numbers")    


# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()




# Program 41: Find Frequency of Each Character
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         freq = {}
#         for i in self.text1:
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1

#         for i ,count in freq.items():
#             print(f"{i}:{count} ")          



# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()




# Program 42: Find Most Frequent Character
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         freq = {}
#         max_count = 0
#         max =''
#         for i in self.text1:
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1

#         for i ,count in freq.items():
#             if count > max_count:
#                 max_count = count  
#                 max = i      
#         print(max,"apperars",max_count,"times")


# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()



# Program 43: Find Least Frequent Character
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         freq = {}
#         min_count = float('inf')
#         min =''
#         for i in self.text1:
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1

#         for i ,count in freq.items():
#             if count < min_count:
#                 min_count = count  
#                 min = i      
#         print(min,"apperars",min_count,"times")


# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()





# Program 44: Check if All Characters are Unique
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         freq = {}
#         is_unique = True
#         for i in self.text1:
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1

#         for i ,count in freq.items():
#             if count > 1:
#                 is_unique = False
#                 break  

#         if is_unique:       
#             print("String contaion all unique character")
#         else:
#             print("String does not contaion all unique character")
                

# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()




# Program 45: Find First Non-Repeating Character 
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         freq = {}
        
#         for i in self.text1:
#             if i in freq:
#                 freq[i] += 1
#             else:
#                 freq[i] = 1

#         for i ,count in freq.items():
#             if count == 1:
#                 print(i)
#                 break  

        

# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()





# Program 46: Find First Repeating Character
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         freq = set()

#         for i in self.text1:
#             if i in freq:
#                 print(i)
#                 break  
#             freq.add(i)    
        

# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()


# Program 47: Count Distinct Characters 
# class Display:
#     def __init__(self,text1):
#         self.text1 = text1
        
#     def equal(self):
#         freq = set()
#         count = 0

#         for i in self.text1:
#             if i not in freq:
#                 count +=1
#                 freq.add(i)    
#         print(count)

# text1 = input("Enter the string1: ")
# d1 = Display(text1)
# d1.equal()



# Program 48: Check if String Contains Substring
# class Display:
#     def __init__(self,text1,text2):
#         self.text1 = text1
#         self.text2 = text2
        
#     def equal(self):
#         count = 0
#         self.text1 = self.text1.split()
#         for i in self.text1:
#             if i==self.text2:
#                 count += 1
            

#         if count !=0:
#             print("The substring exist in string")
#         else:
#             print("The substring does not exist in string")



# text1 = input("Enter the string: ")
# text2 = input("Enter the substring: ")
# d1 = Display(text1,text2)
# d1.equal()




# Program 49: Reverse String (In-Place
# class Display:
#     def __init__(self,text):
#         self.text = text
#         text2 = self.text[::-1]
#         print(text2)


# text = input("Enter the string:")
# d1 = Display(text)



# Program 50: Reverse Each Word in String
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def count(self):
#         text1 = self.text.split()
#         for i in text1:
#            text2 = i[::-1]
#            print(text2,end=" ")

# text = input("Enter the string:")
# d1 = Display(text)
# d1.count()





# Program 51: Reverse Word Order
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def count(self):
#         text1 = self.text.split()
#         text2 = text1[::-1]
#         for i in text2:
#             print(i,end=" ")
          
# text = input("Enter the string:")
# d1 = Display(text)
# d1.count()



# Program 52: Copy String to Another 
# class Display:
#     def __init__(self,text):
#         self.text = text
#     def count(self):
#         text1 = self.text
#         print("new string:",text1)



# text = input("Enter the string: ")
# d1 = Display(text)
# d1.count()





# Program 53: Concatenate Two Strings 
# class Display:
#     def __init__(self,text1,text2):
#         self.text1 = text1
#         self.text2 = text2
#     def count(self):
#         self.text1 = " ".join([self.text1,self.text2])
#         print("The concatenate string is:",self.text1)



# text1 = input("Enter the string1: ")
# text2 = input("Enter the string2: ")
# d1 = Display(text1,text2)
# d1.count()




# Program 54: Extract Substring (Given Positions) 
# class Display:
#     def __init__(self,a,b,text):
#         self.a = a
#         self.b = b
#         self.text = text
#     def count(self):
#         text1 = self.text.split()
#         list1 = []
#         for i in range(self.a,self.b):
#             list1.append(text1[i])
#         print(" ".join(list1))    


# a= int(input("Enter the position1: "))
# b  = int(input("Enter the position2: "))
# text = input("Enter the text: ")
# d1 = Display(a,b,text)
# d1.count()




# Program 55: Insert String at Position
# class Display:
#     def __init__(self,a,text,insert):
#         self.a = a
#         self.text = text
#         self.insert = insert

#     def count(self):
#         text1 = self.text.split()
#         text1.insert(self.a,self.insert)
#         print(" ".join(text1))  

# a= int(input("Enter the position1: "))
# text = input("Enter the text: ")
# insert = input("Enter the text to insert: ")
# d1 = Display(a,text,insert)
# d1.count()




# Program 56: Delete Characters from Position
# class Display:
#     def __init__(self,a,text):
#         self.a = a
#         self.text = text

#     def count(self):
   
#         text1 = self.text.replace(self.text[0:(self.a+1)],"")

#         print(text1)
# a= int(input("Enter the position1: "))
# text = input("Enter the text: ")
# d1 = Display(a,text)
# d1.count()





# # Program 57: Replace Substring with Another
# class Display:
#     def __init__(self,text,replace1,insert):
#         self.text = text
#         self.replace1 = replace1
#         self.insert = insert

#     def remove(self):

#         self.text = self.text.split()
#         for i in range(len(self.text)):
#             if self.text[i] == self.replace1:
#                 self.text[i] = self.insert
#         print(" ".join(self.text))        


# text = input("Enter the text: ")
# replace1 = input("Enter the replace string: ")
# insert = input("Enter the substring: ")
# d1 = Display(text,replace1,insert)
# d1.remove()




# Program 58: Remove First Word
# class Display:
#     def __init__(self,text):
#         self.text = text
#     def remove(self):
#         text1 = self.text.lstrip()
#         text1 = text1.split()
#         list1 = []
#         for i in range(len(text1)):
#             if i!=0:
#                 list1.append(text1[i])
#         print(" ".join(list1))        

# text = input("Enter the text: ")
# d1 = Display(text)
# d1.remove()




# Program 59: Remove Last Word 
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):
#         text1 = self.text.lstrip()
#         text1 = text1.split()
#         list1 = []
#         for i in range(len(text1)):
#             if i != (len(text1)-1):
#                 list1.append(text1[i])
#         print(" ".join(list1))        

# text = input("Enter the text: ")
# d1 = Display(text)
# d1.remove()






# Program 60: Extract First Word 
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):
#         text1 = self.text.lstrip()
#         text1 = text1.split()
#         print(text1[0])
              

# text = input("Enter the text: ")
# d1 = Display(text)
# d1.remove()





# Program 61: Extract Last Word
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):
#         text1 = self.text.lstrip()
#         text1 = text1.split()
#         print(text1[-1])
              

# text = input("Enter the text: ")
# d1 = Display(text)
# d1.remove()



# Program 62: Extract Nth Word
# class Display:
#     def __init__(self,text,position):
#         self.text = text
#         self.position = position

#     def remove(self):
#         text1 = self.text.lstrip()
#         text1 = text1.split()
#         print(text1[self.position])
              

# text = input("Enter the text: ")
# position = int(input("Enter position: "))
# d1 = Display(text,position)
# d1.remove()





# Program 63: Split String by Space
# class Display:
#     def __init__(self,text):
#         self.text = text
    

#     def remove(self):
        
#         text1 = self.text.split()
#         for i in text1:
#             print(i)
        
# text = input("Enter the text: ")
# d1 = Display(text)
# d1.remove()





# Program 64: Join Array of Words into String
# class Display:
#     def __init__(self,n):
#         self.n = n

#     def element(self):

#         list1 = []
#         for i in range(self.n):
#             i = input("Enter the list element: ")
#             list1.append(i)
#         print(list1)
#         return list1    

#     def remove(self,list1):

#         text = " ".join(list1)
#         print(text)

# n = int(input("Enter the size of list: "))
# d1 = Display(n)
# list1 = d1.element()
# d1.remove(list1)



# Program 65: Shift Characters Left by K
# class Display:
#     def __init__(self,text,k):
#         self.text = text
#         self.k = k

#     def remove(self):

#         text1 = self.text
#         print(text1[self.k:] + text1[:self.k])


# text = input("Enter the text: ")
# k = int(input("Rotate string by: "))
# d1 = Display(text,k)
# d1.remove()




# Program 66: Shift Characters Right by K 
# class Display:
#     def __init__(self,text,k):
#         self.text = text
#         self.k = k

#     def remove(self):

#         text1 = self.text
#         print(text1[-self.k:] + text1[:-self.k])

# text = input("Enter the text: ")
# k = int(input("Rotate string by: "))
# d1 = Display(text,k)
# d1.remove()






# Program 67: Swap First and Last Character
# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):

        
#         text1 = self.text[-1]+self.text[1:-1]+self.text[0]
      
#         print(text1)   

# text = input("Enter the text: ")
# d1 = Display(text)
# d1.remove()




# Program 68: Sort Characters in String (Ascending)

# class Display:
#     def __init__(self,text):
#         self.text = text

#     def remove(self):
   
#         text1 = sorted(self.text)
#         print("".join(text1))

# text = input("Enter the text: ")
# d1 = Display(text)
# d1.remove()