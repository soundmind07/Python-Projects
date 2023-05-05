"""
Project Learnings:-
1- used if else statements to decide which block has to be executed based upon decision.
2- used list data structure
3- used while loop along with break and continue statements.
"""




import random

user_wins=0
computer_wins=0

options=["rock","paper","scissors"]

while True:
    user_input=input("Type rock/paper/scissors or q to quit: ").lower()
    if user_input=="q":
        break
    
    if user_input not in options:
        continue

    random_number=random.randint(0,2)

    #0 means its a rock, 1 means its a paper, 2 means its a scissors
    computer_pick=options[random_number]

    print("Computer picked ", computer_pick + ".")

    if(user_input=="rock" and computer_pick=="scissors"):
        print("You won !")
        user_wins+=1
    elif(user_input=="paper" and computer_pick=="rock"):
        print("You won !")
        user_wins+=1
    elif(user_input=="scissors" and computer_pick=="paper"):
        print("You won !")
        user_wins+=1
    else:
        print("You lost")
        computer_wins+=1



print("You won",user_wins,"times.")
print("Computer wins",computer_wins,"times.")

print("GoodBye! ")



