#We again use the random function here. 
# You make a move first and then the program makes one.
#  To indicate the move, you can either use a single alphabet or input an entire string. 
# A function will have to be set up to check the validity of the move.

import random

def play():

    rules = "Rules: paper beats rock, rock beats scissor, scissor beats paper.. and so on.."
    print(rules)
    choices = ['p', 'r', 's']

    user_input = input("(p) For Paper, (r) for rock, (s) for scissor:  ")
    comp_input = random.choice(choices)

    if user_input == comp_input:
        print(f'Computer Choose {comp_input} and You Choose {user_input} so It\'s tie')
    elif (user_input == 'p') and (comp_input == 'r'):
        print(f'Computer Choose {comp_input} and You Choose {user_input} Yay, You Win')
    elif (user_input == 'r') and (comp_input == 's'):
        print(f'Computer Choose {comp_input} and You Choose {user_input} Yay, You Win')
    elif (user_input == 's') and (comp_input == 'p'):
        print(f'Computer Choose {comp_input} and You Choose {user_input} Yay, You Win')
    else:
        print(f'Computer Choose {comp_input} and You Choose {user_input} Yay, Computer Win')

play()