a = int(input("Enter the value: "))
print(type(a))

while a>0:
    print(a)
    a = a-1

for i in range(0,5):
    print("Value of i in loop is: ",i)

for i in range(6,0,-2):
    print("Value of i in loop is: ",i)  

list = [1,2,3,4.5,6.7,"bhoomi",True]
print(list)
print(type(list[4]))

list = [15,27,38,44,56,68]
print(list)
print(list[4])
print(list[-4])

list = [1,2,3,4,5,6]
for i in list:
    print("Value of i:",i)
print("Reverse order:-")
for i in range(-1,-7,-1):
    print("Value is:",list[i])

#if a%2==0 and a>0:
  #  print("It is even")
   # print("Part of if statement......")
#else:
   # print("It is odd")
#print("Bhoomika")        


#a = input("Enter your name: ")
#print(type(a))
#print(a)