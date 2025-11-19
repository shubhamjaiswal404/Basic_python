print("Enter num1")
num1 = int(input())
print("Enter num2")
num2 = int(input())

print("The sum of these two number is , num1 + num2")
print(num1 + num2)

# try - except exception handeling --> convert --> error into --> string
# If I enter the value e which is not a number , I get error but there are code after that also which does not run

try:
    print("The sum of these two number is " , int(num1) + int(num2) )
except Exception as e:
    print(e)

print("This line is very important")
