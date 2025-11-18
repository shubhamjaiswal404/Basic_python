# List function on google

# Slicing does not change original list
# Sort , Reverse change original list

#[] square bracket is list
#() paranthsis bracket is tuple

grocery = [ "Harpic" , "Vim Bar " , "Deodrant" , "Dettol" , "Lollypop" ]

print(grocery)

grocery = [ "Harpic" , "Vim bar " , "Deodrant" , "Dettol" , "Lollypop" , 56 ]

print(grocery[0])
print(grocery[1])
print(grocery[3])
print(grocery[5])
#print(grocery[6]) # Error because list as 0 to 5 index


numbers = [ 2, 7 , 9 , 11 , 3]

print(numbers)

print(numbers[2])

#print(numbers.sort()) # None

numbers.sort()

print(numbers)

numbers.reverse()

print(numbers[0:5]) # start from index 0 to index 5

print(numbers[ :5]) # start from index 0 to index 5 , default is 0 start of list

print(numbers[0: ]) # start from index 0 to index 5 , default is 5 end of list

print(numbers[1: ]) # start from index 1 to index 5

print(numbers[1:4]) # start from index 1 to index 4

print(numbers)

print(numbers[ : : 1]) # skip one element and print whole list

print(numbers[ : : 2]) # skip two element and print whole list

print(numbers[ : : -1]) # reverse list

print(numbers[1 :5 : 2]) # start from index 1 to index 5,skip two element

print(len(numbers)) # length of list

print(max(numbers)) # maximum value in list

print(min(numbers)) # minimum value in list

numbers.append(70)

numbers.append(71)

# numbers = [ ]  --> List

numbers.insert(1,67) # insert function   .insert(x,y)   x --> index , y --> value

print(numbers)

numbers.remove(9)

print(numbers)

numbers.pop() # remove one element

print(numbers)

numbers[1] = 98 # replace index element

print(numbers)

# Mutable - can change --> List []
# Immutable - cannot change --> Tuple ()

tp = ( 1, 2 , 3)
print(tp)

# tp[1] = 8 # error Immutable

# tp = (1) # not a tuple one element

tp1 = ( 1, ) # tuple one element
print(tp1)

a = 1
b = 8
#swap of a and b
temp = a
a = b
b = temp

print(a,b)

#swap of a and b
a,b = b,a
print(a,b)





