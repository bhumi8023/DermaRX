
# Program 116: Longest Consecutive Sequence
# class Product:

#     def __init__(self,n):
#         self.n = n

#     def array1(self):

#         list1 = []
#         for i in range(self.n):

#             i = int(input("Enter the element of list: "))
#             list1.append(i)

#         list1.sort()
#         print(list1)
#         return list1

#     def product1(self,list1):

#         count = 1
#         max = 0
#         for i in range(len(list1)-1):
#             if list1[i]==list1[i+1]-1:
#                 count +=1
#                 if max < count:
#                     max = count
#             else:
#                 count = 1
#         print(max)                

# p1 = Product(10)
# list1 = p1.array1()
# p1.product1(list1)





# Program 117: Product of Array Except Self 

# class Product:

#     def __init__(self,n):
#         self.n = n

#     def array1(self):

#         list1 = []
#         for i in range(self.n):

#             i = int(input("Enter the element of list: "))
#             list1.append(i)
#         print(list1)
#         return list1

#     def product1(self,list1):

        
#         result = []
#         for i in range(len(list1)):
#             prod = 1
#             for j in range(len(list1)):
#                 if i !=j:
#                     prod = list1[j]*prod
#             result.append(prod)
#         print(result)

# p1 = Product(6)
# list1 = p1.array1()
# p1.product1(list1)





# Program 118: Shuffle Array 
# import random
# class Shuffle:
#     def __init__(self,list1):

#         self.list1 = list1

#         for i in range(len(list1)-1,0,-1):

#             j = random.randint(0, i)

#             list1[i] , list1[j] = list1[j] ,list1[i]
#         print(list1)    

# list1 = [1,2,3,4,5,6]
# s1 = Shuffle(list1)




# Program 121: Subarray with Maximum XOR
# class display:
#     def __init__(self):
#         pass
        

#     def operator(self,list1):
#         max_xor = 0
#         for i in range(len(list1)):
#             xor = 0
#             for j in range(i,len(list1)):
#                 xor ^= list1[j]
#                 max_xor = max(max_xor,xor)
#         print(max_xor)

# list1 = [1,2,1,2,3,5,4]
# d1 = display()
# d1.operator(list1)






#  Program 123: Find All Triplets with Sum Zero 
# class Product:

    # def __init__(self,n):
    #     self.n = n

    # def array1(self):

    #     list1 = []
    #     for i in range(self.n):

    #         i = int(input("Enter the element of list: "))
    #         list1.append(i)
    #     print(list1)
    #     return list1

#     def product1(self,list1):

#         result = []
#         for i in range(len(list1)):
#             for j in range(i+1,len(list1)):
#                 for k in range(j+1,len(list1)):
#                     if i!=j or j!=k or k!=i or i!=j!=k:
#                         if list1[i]+list1[j]+list1[k]==0:
                            
#                             result.append(([list1[i], list1[j], list1[k]]))
                               
#         print(result)
                        

# p1 = Product()
# list1 = [-1, 0, -1, 1, 2, -4]
# p1.product1(list1)

