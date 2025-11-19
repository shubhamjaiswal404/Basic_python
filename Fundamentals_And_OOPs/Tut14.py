a = 9
b = 8
#c = sum(a,b) # Error use list or turple

c = sum((a,b)) # built in function
d = sum([a,b]) # built in function

print(c)
print(d)


# user define function::

def function1():
    print("Hello you are in function 1 ") # indentation is used


print("****function1****")
print(function1())
print("***END***")


def function3(a,b):
    print("Hello you are in function 3 ", a + b)


print("**** function3 ****")
function3(5,7)
print(function3(5,7))
print("***END***")


#Now we are going to learn return value

#without return value function2()

def function4(a,b):
    average = (a+b)/2
    print(average)


print("**** function4 ****")
v = function4(5,7) # --> 6.0
print(v)  # --> None
print("***END***")


#with return value function2()
def function2(a,b):
    """
    This is a function which will calculate average of two numbers   --> This is Doc string used because 100's of functions in python program

    This a function which will calculate average of two number this function doesn't work for three numbers
    """

    average = (a+b)/2
    print(average)
    return average

# function for code reusibilty , function name is changed that is error, Or find Error, variable name should same as function name

print("**** function2 ****")
v = function2(5,7) # --> 6.0
print(v) #--> 6.0
print("***END***")

print(function2.__doc__)
