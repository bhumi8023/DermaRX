# 1. class Prime:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def calculation(self):
#         index = 2
#         count = 0
#         a_value = 0
#         b_value = 0
        
#         while count < self.y:
#             if index == 2:
#                 count += 1
#                 if count == self.x:
#                     a_value = index
#                 if count == self.y:
#                     b_value = index
#                 index += 1
#                 continue

#             for i in range(2, index):
#                 if index % i == 0:
#                     break
#                 elif i == index - 1:
#                     count += 1
#                     if count == self.x:
#                         a_value = index
#                     if count == self.y:
#                         b_value = index
#             index += 1
            
#         print(a_value + b_value - 1)

# p1 = Prime(3, 4)
# p1.calculation()




# 2. Minimum value 
# class Matrix:

#     def __init__(self,row,column):
#         self.row = row
#         self.column = column

#     def Minimum(self):

#         matrix =[]
#         print(f"Enter a {self.row}x{self.column} matrix:")

#         for i in range(self.row):
#           row_input = list(map(int, input().split()))
          
#           matrix.append(row_input)
        
#         min_val = matrix[0][0]
#         for i in matrix:

#             for j in i:
            
#              if j < min_val:
#                 min_val = j

    
#         return min_val

# m1 = Matrix(3,3)
  
# print(m1.Minimum())    




# 3.temperature average temprature
# class Temperature:

#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def average(self):

#         aver = 0
#         temp = 0
#         if -100 <= self.x <= 100 and  -100 <= self.y <= 100:
#             if self.x < 10 or self.y <10:
#                 print("It's very cold")
#             if 10 <= self.x  <= 20 or 10 <= self.y <= 20:
#                 print("It's cold")     
#             if self.x > 20 or self.y > 20:
#                 print("It's Warm")

#         aver = (self.x + self.y)/2
#         print(aver)

#         temp = self.x
#         self.x = self.y
#         self.y = temp
#         print(self.x,self.y)

        

# t1 = Temperature(5,25)
# t1.average()
        



#5. 2D array row based on even/odd row index

# class Evenodd:

#     def __init__(self,row,column):
#         self.row = row
#         self.column = column

#     def check(self):

#         matrix = []

#         for i in range(self.row):
#             row_input = list(map(int, input().split()))

#             matrix.append(row_input)

#         for idx,self.row in enumerate(matrix):
#              if idx % 2==0:
#                 for j in self.row:
#                     print(j,end=" ")
#              else:
#                for j in self.row[::-1]:
#                     print(j,end=" ")

# e1 = Evenodd(4,4)
# e1.check()






# 7. difference 
# class difference:

#     def __init__(self,size):
#         self.size = size

#     def height(self):

#         arr = []
#         diffs = set()
       
#         for i in range(self.size):
#             num = int(input("Enter element: "))
#             arr.append(num)
#             if num < 0:
#                  print("invalid")
#                  return 
#         print(arr)     

  
#         for i in range(len(arr)-1):
#             diff = arr[i+1] - arr[i]
#             if diff not in diffs:
             
#                 diffs.add(diff)    
          

#         if len(diffs)==1:
#              print(diff)
#         else:
#             print("none") 
                    


# d1 = difference(4)
# d1.height()         



# 8. permutation of string
# class Permutation:
#     def __init__(self,list1):
#         self.list1 = list1

#     def check(self):

        
        





# 9. Standard deviation of an array

# class Standard:


#     def __init__(self,n):
#         self.n = n

#     def average(self):

#         arr = [] 
#         mean = 0

#         for i in range(self.n):
#             num = int(input("Enter element: "))
#             arr.append(num)
    
#         print(arr) 
#         mean = (sum(arr))/len(arr)
#         print(mean)

#         return arr,mean

#     def deviation(self,arr,mean):

#         diff = 0
#         sqr  = 0
#         total_sqr = 0
#         for i in arr:
#             diff = i - mean
#             sqr = diff **2
#             total_sqr += sqr

#         variance = total_sqr/len(arr)  

#         devi = variance**0.5
#         print(devi)

# s1 = Standard(6)
# arr,mean =s1.average()
# s1.deviation(arr,mean)







# 11. Anagram checker

# class Check:

#     def __init__(self,str1,str2):
#         self.str1 = str1
#         self.str2 = str2

#     def Anagram(self):

#         a = sorted(self.str1)   
#         b = sorted(self.str2)

#         if a==b:
#             print("Anagram")
#         else:
#             print("Not Anagram")       

# c1 = Check("listen","world")
# c1.Anagram()




# 12 Sum of mth amnd n prime numbver
# class Prime:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def calculation(self):
#         index = 2
#         count = 0
#         total = 0

#         z = self.x+self.y
#         while count < z:
#             if index == 2:
#                 count += 1
#                 if count >= self.x and count <= z:
#                    total += index
#                 index += 1
#                 continue

#             for i in range(2, index):
#                 if index % i == 0:
#                     break
#                 elif i == index - 1:
#                     count += 1
#                     if count >= self.x and count <= z:
#                         total += index
#             index += 1
            
#         print(total)

# p1 = Prime(6,2)
# p1.calculation()







# 13. validate prime matrix

# class Matrix:

#     def __init__(self,row,column):
#         self.row = row
#         self.column = column

#     def input(self):

#         matrix1 = []

#         for i in range(self.row):
#             row_input = list(map(int, input().split()))

#             matrix1.append(row_input)
#         if self.row <=0 and self.column <= 0: 
#             print("Wrong Input")

        # if self.row * self.column != len(matrix1): 
        #     print("Wrong Input")
    

#         return matrix1
    
#     def prime(self,matrix1):

#         count = 0
        
#         for i in matrix1:
#             for j in i:
#                 if j<0:
                    
#                     print("Wrong input")
#                 for k in range(2,(j//2)+1):
#                     if j%k == 0:
#                         count += 1   
#         if count != 0:
#             print("Valid")
#         else:
#             print("Invalid")

# m1 = Matrix(2,3)
# matrix1 = m1.input()
# m1.prime(matrix1)




# 21. Find lLCM 
# class Multiple:

#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def gcd(self):

#         x,y = self.a,self.b
#         while y :
#             x ,y = y,x % y

#         return x
    
#     def lcm(self):

#         return (self.a*self.b) //self.gcd()
            
# c1 = Multiple(8,1000000000)
# c1.gcd()
# print("lcm:",c1.lcm())




# 36. Maximum sum of k size subarray


# class Subarray:
#     def __init__(self,n,k):
#                 self.n = n
#                 self.k = k

#     def array(self):
#         list1  = []

#         for num in range(self.n):
#             num =  int(input("Enter the element:"))
#             list1.append(num)
#         print(list1)
#         return list1   
       
#     def maximum(self,list1,k):

#         maxi = 0
#         list2 = []
#         result = []
#         for i in range(len(list1)):
#               if list1[i] %2 ==0:
#                 list1[i] = list1[i]-1
#                 list2.append(list1[i])
#               else:
#                     list2.append(list1[i]) 

               
#         print(list2)        
#         for i in range(len(list2)-k+1):

#             new_array = list2[i:i+k]
           
#             maxi = max(new_array)
#             if maxi not in result:
#                 result.append(maxi)
  
            
#         print(sum(result))    
          

# s1 = Subarray(7,3)
# list1 = s1.array()
# s1.maximum(list1,3)






# 37. Sum of Unique Element

# class Unique:
#     def __init__(self,n):
#         self.n = n

#     def array(self):

#         list1 = []
#         for num in range(self.n):
#             num =  int(input("Enter the element:"))
#             list1.append(num)
        
#         return list1   

#     def calculation(self,list1):

#         list2 = []
#         list1.sort()
#         print(list1)
#         for i in list1:
#             if list1.count(i)==1:
#                 list2.append(i)
#         total = sum(list2)
#         print(total)     

# u1 = Unique(4)
# list1 = u1.array()
# u1.calculation(list1)






# 38. Maximum Subarray

# class Maximum:

#     def __init__(self,n):
#         self.n = n

#     def array(self):

#         list1  = []
#         for num in range(self.n):
#             num =  int(input("Enter the element:"))
#             list1.append(num)  
#         print(list1)    
#         return list1      

#     def subarray(self,list1):

#         max_sum = float('-inf')
         
#         for i in range(len(list1)):
#             total = 0  
#             for j in range(i,len(list1)):
#                 total += list1[j]
#                 if total > max_sum:
#                     max_sum = total
#         print(max_sum)            

# m1 = Maximum(5)
# list1 = m1.array()
# m1.subarray(list1)




# 49. missing value

# class Missing:
#         def __init__(self,n):
#                 self.n = n

#         def array(self):

#            list1  = []
#            for i in range(self.n):
#              num =  int(input("Enter the element:"))
#              list1.append(num)

#            list1.sort()    
#            print(list1)
#            return list1   

#         def value(self,list1):

#              for i in range(len(list1)-1):
#                   if list1[i+1] != list1[i]+1:
#                        print(list1[i]+1)

# m1 = Missing(5)
# list1 = m1.array()
# m1.value(list1)
                       





# 51. Majority element

# class Majority:
#     def __init__(self,n):
#         self.n = n

#     def calculation(self):

#         list1 = []

#         for i in range(self.n):
#             num =  int(input("Enter the element:"))
#             list1.append(num)
#         print(list1)
#         return list1  
    
#     def major(self,list1):

#         count = self.n//3
#         total = 1
#         list1 = sorted(list1)
#         print(list1)
#         for i in range(len(list1)-1):
#                 if list1[i]==list1[i+1]:
#                      total += 1
#                 else:
#                      if total >= count:
#                           print(list1[i]) 
#                      total = 1          
#         # if total > count:
#         #          print(list1[-1])     

# m1 = Majority(9)
# list1 = m1.calculation()
# m1.major(list1)






# 55. divisiible by 9

# class Divisible:

#     def __init__(self,n):
#         self.n = n

#     def check(self):
#         if (self.n)%9 ==0:
#             print("It is divisible by 9")
#         else:    
#             print("It is not divisible by 9")
# d1 = Divisible(286)
# d1.check()



# 56. Max difference

# class Difference:

#     def __init__(self,n):
#         self.n = n

#     def array(self):

#         list1 = []

#         for num in range(self.n):
#             num =  int(input("Enter the element:"))
#             list1.append(num)
#         print(list1)
#         return list1  
    
#     def calculation(self,list1):

#         diff = 0
#         minimum = min(list1)
#         maximum = max(list1)

#         diff = maximum - minimum
#         print(diff)

# d1 = Difference(7)
# list1 = d1.array()
# d1.calculation(list1)



# 59. fibonacci series

# class Fibonacci:

#     def __init__(self,n):
#         self.n = n
#     def series(self):
#         a = 0
#         b = 1
#         total = 0
#         for i in range(0,self.n):
#             total += a
#             a , b = b,a+b
#         print(total)
# f1 = Fibonacci(5)       
# f1.series()     
         






# 57. Data query

# class Data:

#     def student(self):
#         list1 = [
#             {"name":"Alice","age": 22 ,"gender":"female","grade":85.5},
#             {"name":"Bob","age": 18 ,"gender":"male","grade":78.0},
#             {"name":"Charlie","age": 24 ,"gender":"male","grade":92.2},
#             {"name":"Daisy","age": 21,"gender":"female","grade":88.5},
#             {"name":"Eve","age": 18 ,"gender":"female","grade":76.0}
#         ]
#         return list1

#     def calculation(self,list1):

#         total = 0
#         count = 0
#         for i in list1:
#             if i["gender"]=="female":
#                 print(i['name'],end=",")
#         print()        

#         for i in list1:  
#             if i["gender"]=="female":
#                 total += i["grade"]
#                 count += 1
                
#         average = total/count
#         print(f"{average:.2f}")


# d1 = Data()
# list1 = d1.student()
# d1.calculation(list1)






# 58. majority element n/2

# class Majority:

#     def __init__(self,n):
#         self.n = n

#     def array(self):
         

#         list1 = []

#         for num in range(self.n):
#             num =  int(input("Enter the element:"))
#             list1.append(num)
#         print(list1)
#         return list1  
    
#     def major(self,list1):

#         count = self.n//2
#         total = 1
#         list1 = sorted(list1)
#         print(list1)
#         for i in range(len(list1)-1):
#                 if list1[i]==list1[i+1]:
#                      total += 1
#                 else:
#                      if total >= count:
#                           print(list1[i]) 
#                      total = 1          
#         if total >= count:
#                  print(list1[-1])     

# m1 = Majority(6)
# list1 = m1.array()
# m1.major(list1)


# 60 . print table sum

# class Table:

#     def __init__(self,n):
#         self.n = n

#     def calculation(self):

#         total = 0
#         multiply = 0
#         for i in range(1,11):
#             multiply = self.n * i
#             print(self.n,"*",i,"=",multiply)
#             total += multiply
#         print(total)
# t1 = Table(10)
# t1.calculation()   





# 61. Mximum window

# class Maximum:
#         def __init__(self,n,k):
#                 self.n = n
#                 self.k = k

#         def array(self):
#                 list1  = []

#                 for i in range(self.n):
#                        num =  int(input("Enter the element:"))
#                        list1.append(num)
#                 print(list1)
#                 return list1      
#         def subarray(self,list1,k):

#                 maxi = 0 
#                 result = []

#                 for i in range(len(list1)-k+1):
#                         new_array = list1[i:i+k]
#                         maxi = max(new_array)
#                         result.append(maxi)
#                 print(*result)        



# m1 = Maximum(6,3)
# list1 = m1.array()  
# m1.subarray(list1,k=3)                        





# 62. sum of cubes in range

# class Cube:

#     def __init__(self,n,m):
#         self.n = n
#         self.m = m
#     def calculation(self):

#         cube = 1
#         total = 0
#         for i in range(self.n,self.m+1):
#             cube = i*i*i    
#             print(i,"=",cube)
#             total += cube
#         print(total)
# c1 = Cube(4,9)
# c1.calculation()            



# Armstrong Number

# class Number:

#     def array(self,n):

#         self.n = n
#         list1  = []

#         for num in range(self.n):
#           num =  int(input("Enter the element:"))
#           list1.append(num)
#         print(list1)
#         return list1  

#     def length(self,num):

#         length = 0
#         while num > 0:
           
#             length += 1
#             num = num // 10

#         return length
        
#     def armstrong(self,list1):

#         armstrong_list = []

#         for i in list1:
#             length = self.length(i)
#             sum = 0
#             temp = i

#             while temp > 0:
#                 digit = temp % 10
#                 sum += digit ** length
#                 temp = temp // 10
            
#             if sum == i:
#                 armstrong_list.append(True)
#             else:
#                 armstrong_list.append(False)

#         print(armstrong_list)
                
# s1 = Number()
# list1 = s1.array(3)
# s1.armstrong(list1)
       
       
#52. sort colors

# class Color:

#     def __init__(self,n):
#         self.n = n

#     def calculation(self):

#         list1 = []
#         for num in range(self.n):
#           num =  int(input("Enter the element:"))
#           list1.append(num)
#         print(list1)
#         return list1
    
#     def sorting(self,list1):

#         low = 0
#         mid = 0
#         high = self.n - 1

#         while mid <= high  :
#             if list1[mid] ==3:
#                 list1[low], list1[mid] = list1[mid], list1[low]
#                 low += 1
#                 mid += 1
#             elif list1[mid] == 7:
#                 list1[mid], list1[high] = list1[high], list1[mid]
#                 high -= 1
#             else:
#                 mid += 1
#         print(list1)            

# c1 = Color(7)
# list1 = c1.calculation()
# c1.sorting(list1)