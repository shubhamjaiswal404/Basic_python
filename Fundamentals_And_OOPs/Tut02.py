print("Hello")

var1 = "Hello World" #string

print(var1)

var2 = 4    #int
var3 = 36.7 #float

#type() is for datatype of varibale
print(type(var1))
print(type(var2))
print(type(var3))

#print(var1 + var2) # Error
print(var2 + var3)

var4 = " John Oliver"

print(var1 + var4) # string concatenation

var1 = "30"   # string
var4 = "50"   # string

print(int(var1) + int(var4)) #type casting var1 and var2 to integer { converting from string to integer}

"""
To switch variable
str() typecasting to string
int() typecasting to integer
float() typecasting to float
"""
print ("**** Printing Hello World 10 times  ****")
print(10*"Hello World \n") # 10*"Hello World" is to print Hello World 10 time

print(100*int(var1) + int(var4))
print(10*(str(int(var1) + int(var4)) + "\n") )

print("**** Calculator ****")
print("Enter your number")
inpnum = input()  # input is taken is string
print("You entered",inpnum)

print("\n\nEnter first number")
n1 = input()
print("Enter second number")
n2 = input()
print("Sum of these two number is ", int(n1) + int(n2))

