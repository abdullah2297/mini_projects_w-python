# Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. 
# Then give users a hint to guess the number. 
# Every time the user guesses wrong, he gets another clue, and his score gets reduced. 
# The clue can be multiples, divisible, greater or smaller, or a combination of all.

import random

def guessing(x):
    comp_guess = random.randint(1,x)
    user_guess = 0
    while user_guess != comp_guess:
        user_guess = int(input(f"Enter number from 1 and {x}: "))
        if user_guess > comp_guess:
            print("Sorry, Your Guessing is Wrong! ")
            print('So High')
        elif user_guess < comp_guess:
            print("Sorry, Your Guessing is Wrong! ")
            print('So Low')

    print(f"Yay! Your Gussing {user_guess} is Correct" )

guessing(100)

print("=========================")
print("Now computer will guess")
print("=======================")


def comp_gussing(x):

    print("Hello, Choose number from 1 to 100 in your Mind")
    low = 1
    high = x
    feedback = ''
    i = 7
    while feedback != 'c':
        i-=1
        guess = random.randint(low,high)
        feedback =  input(f"Is {guess} High Enter (h)? if low: (l)? if correct enter (c)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        if i == 0:
            print(f"Game Over !!! " )
            break;
    else:
        print(f"Yay! My Gussing {guess} is Correct" )

comp_gussing(100)