f = open("TestFile2.txt")
print(f.readline()) # read one line
print(f.readline()) # read one line
print(f.tell()) # where file pointer is
print(f.tell())
f.seek(0) # file pointer restart from starting of file
print(f.tell())

f.close
