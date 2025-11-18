mystr = "John Oliver is a Businessman"
print(mystr)

print(mystr[4]) #Error
print(mystr[0:4]) # 0 to 4 , 0 include 4 is exclude, use for string slicing

print(len(mystr)) # length of index

#print(mystr[78]) #Error , there is no 78

print(mystr[0:78]) # No Error (Exception)



"""
[0:5:2] --> skip one character interval between 0 2 4 6 8
[0: ] --> blank then default last value of length
[ :5] --> blank then default zero
[0:5: ] --> blank then default one
[ :  : 2 ] --> interval of two skip one character
[x : y:  z]  , x--> 0 , y--> last value of length , z --> interval of one

  0   1   2   3    4   5   6   7   8   9  10  11     --> [ 6:10]
| M | o | n | t | y |    | P | y | t | h | o | n |  |  |
 -12 -11 -10 -9   -8  -7  -6  -5  -4  -3  -2  -1     --> [-12:-7]

 """
print(mystr[-1:0])
print(mystr[-4: ])
print(mystr[-4:-2])

print(mystr[ : : -1]) # reverse string
print(mystr[ : : -2]) # 1st reverse string then skip one character


print(type(mystr)) # string

print(mystr.isalnum()) # False because not a numeric string ,No space in between , return value is boolean

#mystr= "John Oliver is a Businessman"

print(mystr.isalpha())  # False

print(mystr.endswith("Businessman")) # True

print(mystr.endswith("Businesswomen")) # False

print(mystr.count("i"))

#mystr= "John Oliver is a Businessman"

print(mystr.capitalize()) # John oliver is a businessman

print(mystr.find("is")) # 12

print(mystr.lower()) # --> john oliver is a businessman

print(mystr.upper()) # --> JOHN OLIVER IS A BUSINESSMAN

print(mystr.replace("is","are")) # --> John Oliver are a Businessman

print(mystr.replace("a","the")) # -->  John Oliver are the Businessman




