list1 = ["John","Mark","Bill","Steve"]
print(list1[0],list1[1])

# for loop : iteration of list1 , item is element in list1 like :: John ,Mark ,Bill ,Steve
for item in list1:
    print(item) #Note:: Indentation for inside for loop

list2 = [["John",1],["Mark",2],["Bill",6],["Steve",250]]

# for loop : iteration of list2 , item is element in list2 like :: [John,1] ,[Mark,2] ,[Bill,6] ,[Steve,250]
for item in list2:
    print(item) #Note:: Indentation for inside for loop

# for loop : iteration of list2 , item =John, lollypop = 1 ,item =Mark, lollypop = 2 ,item =Bill, lollypop = 6 ,item =Steve, lollypop = 250
for item,lollypop in list2:
    print(item,lollypop)
    print(item,"and lolly is ",lollypop)


dict1 = dict(list2) # typecaste list into dictionary
print(dict1)

for item in dict1:
    print(item)

#for item,lollypop in dict1: # Error { same output but by dictionary }

for item,lollypop in dict1.items():
    print(item,lollypop)


items = [ int, float, "Harry", 5 , 6, 7, 8,9,10,11,12,13]

for item in items:   
    """
    if item.isnumeric() and item>6: # Error
        print(item)
    """

    if str(item).isnumeric() and item > 9:
        print(item)

    if str(item).isnumeric() and item >= 9:
        print(item)
