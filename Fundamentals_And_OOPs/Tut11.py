# no of gusses 9
# print no of guesses left
# game Over
# No of guesses he took to finish

number_of_guesses = 1
print("Number of guesses is limited to only 9 times")

while (number_of_guesses <= 9):
    guess_numbers = int(input("Guess the number :\n"))

    if guess_numbers < 18 :
        print("You enter less number please input greater number \n ")

    elif guess_numbers > 18 :
        print(" you enter greater number please input small number \n")

    else:
        print("you won \n")
        print(number_of_guesses , " no of guesses he took to finish " )

        break
    print( 9 - number_of_guesses , " no of guesses left ")

    number_of_guesses = number_of_guesses + 1

if(number_of_guesses > 9) :
    print("Game Over")

