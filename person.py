# class Person:
    
#     def display():
#         print("Hiiii")


# p1 = Person()
# p1.name = "Bhumi"
# p1.age = 20
# p1.college = "Sage University"

# print("My name is:",p1.name)
# print("My age is:",p1.age)
# del p1.age     #used to remove an attribute
# print("My age is:",p1.age)

# p2 = Person()
# p2.salary=12000


# class Solution:
#     def getMinMax(self, arr):
        
#         arr = sorted(arr)
#         for i in arr:
#              minimum = arr[0]
#              maximum = arr[0]
#              if 1<= len(arr)<= 100000 and 1<= i <= 1000000000 :
#               if maximum < i:
#                    maximum = i
#         for i in arr:
#             if 1<= len(arr) <= 100000 and 1<= i <= 1000000000 :
#                 if minimum > i:
#                     minimum = i
                    

#         print("Max:",maximum,"Min:",minimum)
# s1 = Solution()
# arr = [1,5,9,8,4,6]
# s1.getMinMax(arr)


class Solution:
    def findDuplicates(self, arr):
        arr = sorted(arr)

        for i in arr:
            if 1<= len(arr) <= 10**6 and 1<= i <= len(arr):
                



s1 = Solution()
arr = [2,3,1,3,2]
