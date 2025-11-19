f = open("TestFile1.txt","w")
f.write("Statement 1 writting in file \n ")
f.close() # always close the file

#f = open("TestFile2.txt","w")
f = open("TestFile2.txt","a") # a --> add Message in TestFile2.txt
f.write("Statement 1 writting in file \n")
a = f.write("Statement 2 writting in file \n " )
print(a) # number of character return value
f.close()



f = open("TestFile1.txt","a")
a = f.write("Statement 2 writting in file \n " )
print(a)
f.close()

# Handle read and write both+
#"+r" --> Read and write both
# harry2.txt --> file name

f = open("TestFile2.txt" , "r+")
print(f.read()) # read file
f.write("Thank you \n ") # write in file
f.close()

"""
f = open("TestFile1.txt" , "r+")
print(f.read()) # read file
f.write("Thank you \n") # write in file
f.close()
"""
