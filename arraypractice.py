#1. Traverse array 
# array = [1,2,3,4,5,6,7]
# print(array)


#2. reverse array
# array = [1,2,3,4,5,6,7]
# reverse = []
# for i in range(len(array)-1,-1,-1):
#     reverse.append(array[i])
# print(reverse) 

#3,4. array to list
# array = [1,2,3,4,5,6,7]
# list1 = list(array)
# print(list1)

# list1 = set(list1)
# print(list1)

#5. Subaaray of array
# list1 = [1,2,3,4,5,6,7]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)+1):
#         sub = list1[i:j]
#         print(sub)


# #6 sorting
# list1 = [3,7,1,5,2,6,4]
# list1 = sorted(list1)
# print(list1)

#6 searching
# list1 = [1,2,3,4,5,6,7]
# search = 5
# for i in range(len(list1)):
#     if list1[i]==search:
#         print(i)
#         break

#7  insert/delete
# list1 = [1,2,3,4,5,7,8]
# list1.insert(5,6)
# print(list1)

# list1.remove(8)
# print(list1)

# list1.pop(3)
# print(list1)

#8 Merge array
# list1 = [1,2,3,4,5,6]
# list2 = [7,8,9,10]
# list1 = list1 + list2
# print(list1)

#9. duplicate 
# list1 = [1,2,3,4,2,5,6,7]



#selection sort
# list1 = [1,25,78,45,69,52,36]
# right = len(list1)-1
# temp = 0
# min_value = 0
# for i in range(right):
#     min_value = min(list1[i:])
#     temp = list1[i]
#     list1[i] = list1[min_value]
#     list1[min_value] = temp
# print(list1)    




# linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def display(self):
        currentNode = self
        while currentNode != None:
         print(currentNode.data)  
         currentNode = currentNode.nextNode

    def appenend(self,data):
        currentNode = self
        while currentNode.nextNode != None:
          currentNode = currentNode.nextNode

        newNode = Node(data) 
        currentNode.nextNode = newNode
          

n1 = Node(10)

# n2 = Node(20)
# n1.next = n2
# n3 = Node(30)
# n2.next = n3
# n4 = Node(40)
# n3.next = n4
# n5 = Node(50)
# n4.next = n5
# n1.display()
n1.appenend(12)
n1.appenend(58)
n1.appenend(62)
n1.appenend(42)
n1.appenend(52)
n1.display()





# addd new node at end
# class Node:
#     def __init__(self,data=None):
#         self.data = data
#         self.next = None
#         self.head = None

#     def user_input(self):
#         print("Enter the data: ")

#         user_input = list(map(int,input().split()))

#         tail = None

#         for i in user_input:
#             new_node = Node(i)

#             if self.head is None:
#              self.head = new_node
#              tail = new_node
#             else:
#              tail.next = new_node
#              tail = new_node

#         return self.head 
    
#     def append_element(self,data):
#         newnode = Node(data)
#         currentNode = self.head
         
#         while currentNode.next != None:
#             currentNode  = currentNode.next

#         currentNode.next = newnode   

#     def display(self):

#         currentNode = self.head
#         while currentNode != None:
#           print("node data is:",currentNode.data)  
#           currentNode  = currentNode.next
          
# n1 = Node()
# n1.user_input()
# n1.append_element(25)
# n1.display()






#add node at begining
# class Node:
#     def __init__(self,data=None):
#         self.data = data
#         self.next = None
#         self.head = None

#     def user_input(self):
#         print("Enter the data: ")

#         user_input = list(map(int,input().split()))

#         tail = None

#         for i in user_input:
#             new_node = Node(i)

#             if self.head is None:
#              self.head = new_node
#              tail = new_node
#             else:
#              tail.next = new_node
#              tail = new_node

#         return self.head 
    
#     def append_element(self,data):

#         newnode = Node(data)     
#         newnode.next = self.head  
#         self.head = newnode 

#     def display(self):

#         currentNode = self.head
#         while currentNode != None:
#           print("node data is:",currentNode.data)  
#           currentNode  = currentNode.next
          
# n1 = Node()
# n1.user_input()
# n1.append_element(25)
# n1.display()



