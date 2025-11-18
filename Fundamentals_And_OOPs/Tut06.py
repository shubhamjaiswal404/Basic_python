s = set() # Set store unique value
print(type(s))

# Set form List - Method 1
s_from_list1 = set([1,2,3,4])
print(s_from_list1)
print(type(s_from_list1))

# Set form List - Method 2
l = [1,2,3,4]
s_from_list2 = set(l)
print(type(s_from_list2))

# add element
s.add(1)
s.add(2) # set store unique value
s.add(3)
s.add(4)
print(s)

# union of set
s.union({1,2})
s.union({1,2,3})

# given set , s =  { 1, 2, 3 , 4}
# union of set , s1 =  s u { 4, 5, 6} = { 1,2,3,4} u { 4, 5, 6} = { 1, 2, 3, 4, 5, 6}

s1 = s.union({4,5,6})
print(s,s1)

# Intersection of set
s.intersection({1,2})
s.intersection({1,2,3})

# given set , s =  { 1, 2, 3 , 4}
# intersection of set , s1 =  s n { 4, 5, 6} = { 1,2,3,4} n { 4, 5, 6} = { 4 }

s1 = s.intersection({4,5,6})

print(s,s1)

print(len(s))
print(type(s))
print(max(s))
print(min(s))

# check disjoinset

#s1 = s.isdisjoint() --> True or False

# given set , s =  { 1, 2, 3 , 4}
# intersection of set , s1 =  s n { 4, 5, 6} = { 1,2,3,4} n { 4, 5, 6} = { 4 } --> False This is joint set
# intersection of set , s1 =  s n { 5, 6, 7} = { 1,2,3,4} n { 5, 6, 7} = {  } --> True This is disjoint set

s1 = {5,6,7}

print(s.isdisjoint(s1)) # True
print(s,s1)

s.remove(2) # removing 2 from set
print(s)
s.add(6)

print(s.isdisjoint(s1)) # False


