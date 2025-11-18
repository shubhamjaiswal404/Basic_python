var1 = 6
var2 = 56

print("Enter number ?")
var3 = int(input())  # input is string that is converted into integer

#print("Greater") # Error of No indentation inside if ( No space, Note space in python is important )
if var3 > var2:   # if(var1 >var2): ---> Bracket is optional
    print("Greater")  # Indentation is important
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")

# not and in are two different keywords
# in --> inside checker keyword like if
# not --> !(negation) like means NO

list1 = [5,7,3]
if 5 in list1:
    print("Yes its in the list")

print(5 in list1) # true
print(16 in list1) # false

if 15 not in list1:
    print("No its not in the list")

print("No its not in the list")


#Test case:
print("What is your age ?")
age = int(input())

if age < 18:
    print("You cannot drive")
elif age == 18:
    print("We will think about you")
else:
    print("You can drive")








