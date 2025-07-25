# Number Guessing Game
import random # import the random module which is a python generator random tools
# to generate the random number between 1 to 9
secret_number = random.randint(1,9)

# we call the loop which is while loop because we can't know when the user guess the input that's why we uses the while loop
while True:
    guess = int(input("enter the number or guess the number between 1 to 9:"))
    
    if guess == secret_number:
        print("well guessed!")
        break # Exist the loop when one guessed right.
    else:
        print("Try Again!")
   