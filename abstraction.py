
# #abstraction class will be declared and implemention will be defined by child class
# #abstraction hides the information
# for i in range(1,10):
#     if(i%2==0):
#      print(i," is even")
#     else:
#        print(i," is odd")

# N = int(input("Enter N: "))
# #even number
# for i in range(2, (2 * N) + 1, 2):
#     print(i) 

# N = int(input("Enter N: "))

# # odd number
# for i in range(1, (2 * N) + 1):
#     if i % 2 != 0:  
#         print(i)
 
#Divisible by 5
# N = int(input("Enter N: "))
# for i in range(1,N+1):
#     if(i%5==0):
#         print(i)

#table
#N = int(input("Enter the number: "))
#for i in range (1,11):

#    result = i*N
#    print(N,"*", i ,"=",result)

#square of first n number    


# N = int(input("Enter the number: "))
# result = 0
# for i in range(1,N):
#     result = result+i
# print(result)

#array
# list = []
# N = int(input("Enter the number : "))
# for i in range(N):
#     num = int(input("Enter element: "))
#     list.append(num)
# print(list)

#sum of array
# list = [1,2,3,4,5]
# result = 0
# for i in list:
#     result = i +result
# average = result/len(list)
# print("The sum of elments in array is : ",result)
# print("The average is: ",average)    

#Count Elements Greater Than X
# X = int(input("Enter the number: "))
# list = [12,25,47,56,6]
# count = 0
# for i in list:
#     if(X<i):
#      count += 1
# print(count)     

#Program 7: Count Even and Odd Numbers
# list = [1,2,3,4,5]
# counteven = 0
# countodd = 0
# for i in list:
#     if(i%2==0):
#         counteven += 1
#     else:
#         countodd += 1
# print("The count of even number is: ",counteven)
# print("The count of odd number is: ",countodd)

#Check if Element Exists
# list = [1,2,3,4,5]
# X = int(input("Enter the number: "))
# count = 0
# for i in list:
#    if i ==X:
#       count += 1
# if count ==0:
#    print("not found")
# else:
#    print("found")           

# Find Maximum Element
# list = [1,2,3,4,5]
# max = 0
# for i in list:
#     if max<i : 
#         max = i
# print("the maximum element is ",max)

# Find Position of Maximum
# list = [1,2,3,4,5]
# max = 0
# for i in list:
#     if max<i : 
#         max = i
# #for i in list:
# if i==max:             
#         print("the postion is ",list.index(i))

#Linear search
# X = int(input("Enter the number: "))
# list = [1,2,3,4,5]
# count = 0
# for i in list:
#     if i == X:
#         print(X)
#     count += 1
# if count ==0:
#     print("-1")         

#Count Occurrences of Element
# X = int(input("Enter the number: "))
# list = [1,2,3,2,5]
# for i in list:
#     if i ==X:
#         print(list.index(i))
#         break

#Find All Positions of Element
# X = int(input("Enter the number: "))
# list = [1,2,3,2,5]
# for i in range(len(list)):
#     if list[i] ==X:
#         print(i)

#reverse array
# list = [1,2,3,4,5]
# reverse = []
# i = len(list)-1
# while i >=0:
#     reverse.append(list[i])
# print(reverse)    
    

#swap 1 and last
# def list():
#     list1 = [1,2,3,4,5]
#     temp = 0
#     temp = list1[0]
#     list1[0] = list1[-1]
#     list1[-1] =   temp 

#     print(list1)
# list()        

#Program 32: Rotate Array left by 1
# def list1():
#     list = [1,2,3,4,5]
#     temp = 0
#     temp = list[0]
#     for i in range(len(list)-1):
#         list[i]=list[i+1]
#     list[-1]=temp
#     print(list)
# list1()    

# Program 34: Rotate Array Right by K Positions
# def list():
#     list1 = [1,2,3,4,5]
#     k = 2
    
#     n = len(list1)
#     k = k % n
#     for i in range(k):
#         temp = list1[-1] 
        
#         for j in range(n - 1, 0, -1):
#             list1[j] = list1[j- 1]
            
#         list1[0] = temp  
        
#     print(list1)

# list()

#copy array
# def list():
#     list1 = [1, 2, 3, 4, 5]
#     list2 = []
#     for i in range(len(list1)):
#         list2.append(list1[i])
#     print (list2)    
# list()    

#insert elemnt 
# def list1():
#     list = [1,2,3,4,5]
#     element = int(input("Enter the element to insert: "))
#     index = int(input("Enter the index position: "))
#     if index < 0 or index > len(list):
#         print("Invalid index position!")
#       
#     list.append(0) 
#     for i in range(len(list)- 1,index,-1):
#         list[i] = list[i -1]
#     list[index] = element
    
#     print(list)

# list1()

#merge array
# def list():
#     list1 = [1,2,3,4,5]
#     list2 = [6,7,8,9,10]
#     list3 = []
#     for i in range(len(list1)):
#        list3.append(list1[i])
#     for j in range(len(list2)):
#         list3.append(list2[j])
#     print(list3)
# list()       

# Program 42: Concatenate Two Arrays
# def list():
#     list1 = [1,2,3,4,5]
#     list2 = [6,7,8,9,10]
#     list3 = []
#     list3 = list1+list2
#     print(list3)
# list()    

# Program 43: Split Array into Two Equal Parts 
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = []
# list3 = []

# if len(list1) % 2 == 0:
#     mid = len(list1) // 2
    
#     for i in range(0, mid):
#         list2.append(list1[i])
        
#     for i in range(mid, len(list1)):
#         list3.append(list1[i])   
        
#     print(list2)
#     print(list3)

#seprate even and odd number
# list1 = [1,2,3,4,5]
# even = []
# odd = []
# for i in range(len(list1)):
#     if list1[i] % 2 == 0:
#         even.append(list1[i])
#     else:
#         odd.append(list1[i])
# even = even+odd
# print(even)        

#end 0
# list = [1,2,0,3,0,0]
# list1 = []

# for i in range(len(list)):
#     if list[i] != 0:
#         list1.append(list[i])
# for i in range(len(list) - len(list1)):
#     list1.append(0)
# print(list1)

#Write a program that checks if the array is sorted asscending order

# list = [1,2,3,4,5,6]
# count = 0
# for i in range(len(list)-1):
#     if list[i]>list[i+1]:
#         count += 1
#         break 
# if count==0:
#     print("yes , it is sorted")
# else:
#     print("no it is not sorted")        

#Program 47: Check if Array is Sorted (Descending
# list = [6,5,4,3,2,1]
# count = 0
# for i in range(len(list)-1):
#     if list[i]<list[i+1]:
#         count += 1
#         break 
# if count==0:
#     print("yes , it is sorted")
# else:
#     print("no it is not sorted")
        
#Program 40: Replace All X with Y
# list = [1,2,6,4,5,6]
# X = int(input("remove the elemnt: "))
# Y = int(input("insert the element: "))
# for i in list:
#     if list[i]==X:
#         list[i] = Y
# print(list)   

# Program 39: Remove All Occurrences of X 
# list = [1,2,6,3,6,4,5,6]
# list1 = []
# X = int(input("Enter the element: "))
# for i in list:
#     if i != X:
#         list1 += [i]
# print(list1)        

#Program 37: Delete Element at Specific Position
# list = [1,2,3,6,4,5]
# X = int(input("Enter the element: "))
# for i in list:
#     if i == X:
#         list[i]=list[i+1]
# print(list)        

#Program 49: Check if Array is Palindrome
# list = [1,2,3,2,1]
# count = 0
# for i in range(0,len(list)//2):
#     if list[i] == list[i-1]:
#         count += 1
# if count ==len(list)//2:
#     print("Palindrome") 
# else:
#     print("not palindrome")       

#Program 50: Sum at Even Indices

# list = [1,2,3,4,5,6]
# sum = 0
# for i in list:
#     if list.index(i)%2==0:
#         sum = i+sum
# print(sum)        

# Program 51: Sum at Odd Indices 
# list = [1,2,3,4,5,6]
# sum = 0
# for i in list:
#      if list.index(i)%2!=0:
#       sum = i+sum
# print(sum)        

# #Program 52: Difference Between Even and Odd Index Sums
# list = [1,2,3,4,5,6]
# sum_even = 0
# sum_odd = 0
# for i in list:
#    if list.index(i)%2==0:
#       sum_even = sum_even+i
# print("Even index sum is: ",sum_even)   

# for i in list:
#      if list.index(i)%2!=0:
#       sum_odd = i+sum_odd
# print("Odd index sum is: ",sum_odd)  

# sum_even = sum_even-sum_odd
# print("Even index sum is: ",sum_even)  

# #Program 53: Find Range (Max - Min) 
# list = [25,56,47,89,52,4]
# max = 0

# for i in list:
#     if max<i:
#       max = i
# print("The maximum number is: ",max)      
# for i in list:
#     min = i
#     if min>i:
#         min = i
# print("the minimum number is: ",min)
# max = max-min
# print("The difference is: ",max)

# Program 54: Find Second Largest Element
# list = [12,34,56,78,9]
# max = 0 
# second = 0
# for i in list:
#     if i >max:
#         second = max
#         max = i
#     elif i >second and i != max:
#         second = i
# if second!=0:
#     print("The second largest element is: ",second)

#----------------------------24/06/2026--------------------------------------
# Program 55: Find Second Smallest Element
list = [12,34,56,78,9]

min = float('inf')
second = float('inf')
for num in list:
    if num < min:
        second = min
        min = num
    elif num <second and num != min:
        second = num
if second!=0:
    print("The second smallest element is: ",second)


# # Find kth largest element
# list = []
# N = int(input("Enter the number : "))
# for i in range(N):
#      num = int(input("Enter element: "))
#      list.append(num)
# print(list)
# K = int(input("Enter the kth largest number: "))
# max = 0
# for i in list:
#      if K < num:
#           max = num
# print("The maximum number is ", max )          


# Count Elements Greater Than Average
# list = []
# N = int(input("Enter the number : "))
# for i in range(N):
#      num = int(input("Enter element: "))
#      list.append(num)
# print(list)
# sum = 0
# average = 0
# count = 0
# for i in list:
#      sum = sum+i
# print("The sum is: ",sum)
# average = sum/len(list)
# print("The average is: ",average)
# for i in list:
#      if average<i:
#           count +=1
# print("Count of elements greater then average is : ",count)          

#Count Elements Less Than Average
# list = []
# N = int(input("Enter the number : "))
# for i in range(N):
#      num = int(input("Enter element: "))
#      list.append(num)
# print(list)
# sum = 0
# average = 0
# count = 0
# for i in list:
#      sum = sum+i
# print("The sum is: ",sum)
# average = sum/len(list)
# print("The average is: ",average)
# for i in list:
#      if average>i:
#           count +=1
# print("Count of elements smaller then average is : ",count)   


# Find Longest Increasing Sequence Length
# list = []
# N = int(input("Enter the number : "))
# for i in range(N):
#      num = int(input("Enter element: "))
#      list.append(num)

# max_length = 0
# length = 1
# for i in range(len(list) - 1):
#         if list[i] < list[i + 1]:
#             length += 1
#             if max_length < length:
#                   max_length = length
#         else:
#               length = 1
# print(max_length)                  


