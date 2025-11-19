f = open("TestFile2.txt","rt")
print(f.readlines()) # using readline before make the pointer at end then use it any how you can't, restart the file pointer to start of file
f.seek(0)
print(f.readlines())

f.close()

# Not need to close the file
with open ("TestFile2.txt") as f:
    f = open("TestFile2.txt","rt")
    a = f.read(4)
#   a = f.read()
#   a = f.readlines()
    print(a)


