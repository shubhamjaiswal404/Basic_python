#Operators In Python
#Arithmetic Operators
#Assignment Operators
#Comparison Operators
#Logical Operators
#Identity Operators
#Membership Operators
#Bitwise Operators

#Arithmetic Operators
print("Arithmetic Operators")
print("5 + 6 is ", 5+6)
print("5 - 6 is ", 5-6)
print("5 * 6 is ", 5*6)
print("5 / 6 is ", 5/6)
print("5 // 6 is ", 5//6)
print("5 ** 3 is ", 5**3)
print("5 % 6 is ", 5 % 6)

#Assignment Operators   --> value is given to variable
x = 5
print("Assignment Operators")
print(x)

x+=7 # x+=7  --> x = x + 7

print(x)

x%=7 # x=x%7

print(x)

#Comparison Operators  -->Output: True or False used in compasion of two values
print("Comparison Operators")
i = 5
print(i==5) # True
i = 8
print(i==5) # False

print(i>=5) # True

print(i<=5) # False

print(i<5)  # False

print(i>=5) #True

print(i!=5) #True

#Logical Operator --> Output: True or False , AND , OR..
print("Logical Operator")
a = True
b = False

#print(a and a)
print(a and b) #False
print(a or b)  #True

#identity Operator
print("identity Operator")
list1=[1,2]
list2=[1,2]
list3=list1

print(list1 is list2)  # is  compare if two variables refer to the exact same object in memory--> False
print(list1 is not list2 ) # is not  --> True

print(list1 is list3)  #Note:: is  compare if two variables refer to the exact same object in memory == --> True
print(list1 is not list3 ) # is not  --> False

#Membership Operator
print("Membership Operator")
list = [3,3,2,2,39,33,35,32]

print(32 in list) # in --> check inside list given value is present  --> True
print(32 not in list) # not in --> check inside list given value is not present --> False

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print("Bitwise Operators")
print(0 & 1) # and between 00 , 01 --> 00

print(0|1) # or between 00 , 01 --> 01

# Note :: Python file name should not same as python module name

