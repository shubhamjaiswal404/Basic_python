# Google Dictionary function python

# Dictionary is nothing but key value pairs

# key - Immutable --> number , string
# value - mutable --> list , tuple, dictionary

d1 = {}
print(type(d1)) # Dictionary

d2 = {"John":"Burger","Steve":"Fish","Bill":"Roti"}
print(d2)

# print(d2["john"]) #Error
print(d2["John"]) # Case Sensitive

d2 = {"John":"Burger","Steve":"Fish","Bill":"Roti","Allen":{"B":"maggie","L":"roti","D":"Chiken"}}

print(d2["Allen"]["B"])

print(d2["Allen"])

d2["Mark"] = "Junk Food"

print(d2)

d2["Tom"]="Kebabs"

d2[420]="Pizza"

print(d2)

del d2[420]

print(d2)

print(d2.copy())

d3 = d2

print(d3)

del d3["John"]

print(d3)

d3 = d2.copy

print(d2.get("John"))

print(d2.update({"Leena":"Toffee"}))

d2.update({"Leena" : "Toffee"})

print(d2)

print(d2.keys())

print(d2.items())


