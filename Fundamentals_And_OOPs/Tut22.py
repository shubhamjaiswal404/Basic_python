# global - 1
l = 10 # Global Scope

def function1(n):
    l = 5 #Local Scope
    l = l + 45
    global l
    m = 8 #Local
    print(l,m)
    print(n,"I have printed")
    print(l)

print(l)
# print(m) #Error
function1("This is me ")

x = 89
def john():
    x = 20
    def mark():
        global x
        x = 88

    print("Before Calling mark()", x)
    mark()
    print("after calling mark()",x)

john()
print(x)

