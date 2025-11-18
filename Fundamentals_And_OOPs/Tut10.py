j = 0

while(j < 45):
    print(j + 1)
#    print(j + 1, end=" ")
    j = j + 1

#while(True) # Never ending
i = 0
while(True):
    i = i + 1

    if i + 1 < 10:
        print("skip --> continue ")
        continue #It take back to while not going down the code , skip condition and run entire loop

    if( i == 44):
        print("done --> break ")
        break  # Stop the loop (outside the loop )




while(True):
    inp = int(input("Enter a Number\n"))

    if inp > 100:
        print("Congrates you have entered a number greater than 100 \n")
        break
    else:
        print("Try Again! \n")
        continue

