f = open("TestFile.txt") # f is file pointer , "Harry.txt" is name of the file
content = f.read()
print(content)
f.close()


#f = open("TestFile.txt","r")  # read
#f = open("TestFile.txt","rb") # binary form read
f = open("TestFile.txt","rt") # text

content = f.read(3) #  3 --> 344 --> 34455
print(content)
f.close()

f = open("TestFile.txt","rt") # text
content = f.read(34455)
print("2",content)
print("1",content)
f.close()


print("**** Read file character by character ****")

f = open("TestFile.txt","rt") # text
content = f.read() # f pointer is at end of file after f.read()
#print(content)

for line in content: # one - one character
    print(line)


print("**** Read file line by line ****")

f.seek(0) # reset for start of file

for lines in f:  # Normal form but default one line space
    print(lines,end=" ")



print("**** readline() , readlines() ****")

f.seek(0) # reset for start of file
print(f.readline()) # list form read --> read only one line

print(f.readlines()) # after readline() function file pointer is on 2nd line

# File Io Basics
"""
"r" - Open file for reading - default
"w" - Open a file for writting
"x" - Create file if not existd
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"t" - read and write
"""
