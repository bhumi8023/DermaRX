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
import string
class Display:
    def __init__(self,text):
        self.text = text

    def calculation(self):    

        print(string.capwords(self.text)) 

text = input("Enter the string: ")
d1 = Display(text)
