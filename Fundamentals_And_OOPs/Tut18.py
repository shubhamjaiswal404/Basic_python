#Exercise
"""
Pattern Printing
Input = Integer n
*
* *
* * *
* * * *

Boolean = True or False

True n = 4  ( n = n of rows )

False n = 4

* * * *
* * *
* *
*
"""

# Method 1::
print("How many Row You want To Print ")
one = int(input())
print("Type 1 or 0 ")
two = int(input())
new = bool(two)

if new == True :
    for i in range ( 1, one + 1):
        for j in range ( 1 , i + 1) :
            print("*" , end = "")
        print()
elif new == False:
    for i in range (one , 0, -1):
        for j in range (1 , i + 1):
            print("*", end = "")
        print()


print("Pattern printing")
num = int(input("Enter num how many row you want : "))

print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False :")

if bool_val == "1":
    for i in range (0 , num + 1):
        print("*" * int(i))



if bool_val == "0":
    for i in range (num, 0 , -1):
        print("*" * int(i))

# Method 2::
try:
    n = int(input("Enter No of Row : " ))
    b = int(input("Enter Pattern (0 or 1) : "))
 #   if b is 0 :
    if b == 0 :
        count = 0
        while(count <= n):
            print("*"*count,end="")
            print("\n",end= "")
            count = count + 1
            continue

#    elif b is 1:
    elif b == 1:
        count = n
        while(count != 0):
            print("*"*count,end="")
            print("\n",end="")
            count = count - 1
            continue

    else:
        print("Invaild Pattern !!!")

except Exception as e:
    print("Invaild Input!!!")


# Method 3::
n = int(input("enter a number : "))
a = int(input("enter your boolean number:"))

if(bool(a)):
    for i in range( 1, n+1 ):
        for j in range( 1 , i+ 1):
            print("*",end = "")
        print()
else:
    for i in range(1, n+1):
        for j in range(1,n+2-i):
            print("*",end="")
    print()

# Method 4::
def start(a,b):
    a = int(input("Please add number of line you want to print: " ))
    b = bool(int(input("Please add 0 for false")))

    if b == True:
        c = 1
        while c<=a:
            print(c*"*")
            c =c + 1
    else:
        while a>0 :
            print(a*"*")
            a = a -1

start(a,b)
