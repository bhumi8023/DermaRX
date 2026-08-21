#Program 18: Linear Search 
# X = int(input("Enter the number: "))
# list = [1,2,3,4,5]
# flag = False
# for i in list:
#     if i == X:
#         flag = True
#         print("element found on index ",list.index(i))
#         break  
# if flag == False:    
#         print("-1")

#Program 19: Count Occurrences of Element
# X = int(input("Enter the number: "))
# list = [1,2,3,2,5,2,4,8,2,5,6,4]
# count = 0
# for i in list:
#     if i==X:
#         count += 1
# print(count)        

# #Program 20: Find First Occurrence
# X = int(input("Enter the number: "))
# list = [1,2,3,2,5,2,4,8,2,5,6,4]
# for i in list:
#     if i==X:
#         print(list.index(i))
#         break
# if i!=X:
#     print("-1")
  
        
#Program 21: Find Last Occurrence  
# X = int(input("Enter the number: "))
# list = [1,2,3,2,5,2,4,8,2,5,6,4]
# flag = False
# for i in range(len(list)):
#     if list[i]==X:
#         index = i
#         flag = True
# print(index)       
# if flag == False:
#     print("-1")

# # Program 22: Find All Positions of Element
# X = int(input("Enter the number: "))
# list = [1,2,3,2,5,2,4,8,2,5,6,4]
# flag = False
# for i in range(len(list)):
#     if list[i]==X:
#         print(i)
#         flag = True
        
# if flag == False:
#     print("-1")
  
# Program 23: Check for Duplicates
# X = int(input("Enter the number: ")) 
# list = [1,2,3,2,5,2,4,8,2,5,6,4]
# count = 0

# for i in range(len(list)):
#     if list[i]==X:
#         count += 1
# if count > 1:
#     print("Yes")
# else:
#     print("No")

#Program 24: Find First Duplicate
# list = [1,2,3,2,5,2,4,8,2,5,6,4]

# for i in range(len(list)):
#     if list[i]==list[i+1]:
#         print(i)
        


# Program 25: Count Distinct Element    

# list = [1,2,3,2,5,2,4]
# count = 0
# for i in list:
#     flag=False
#     for j in range(0,i):
#         if list[i]==list[j]:
#             flag = True
#             break
#     if flag == False:        
#         count += 1  

# print(count)  

#Program 26: Frequency of Each Element
list1 = [1,2,3,2,5,2,4]

for i in range(len(list1)):
    count = 0
    for j in range(i,len(list1)):
        if list1[i]==list1[j]:        
            count += 1  
        print(i ,"frequency is : ",count)  