"""
Project Learnings:-
1- used if else statements to decide which block has to be executed based upon decision.
"""


print("Welcome to my quiz game ! ")
playing=input("Do u want to play ? ")
if playing.lower()!="yes":
    quit()

print("Okay! Let's play :)")

score=0
#question 1

answer=input("What does cpu stands for ? ")
answer=answer.lower()
if answer=="central processing unit":
    print("Correct !")
    score=score+1
else:
    print("Incorrect ! ")

#question 2

answer=input("What does gpu stands for ? ")
if answer=="graphics processing unit":
    print("Correct !")
    score=score+1
else:
    print("Incorrect ! ")

#question 3

answer=input("What does ram stands for ? ")
if answer=="random access memory":
    print("Correct !")
    score=score+1
else:
    print("Incorrect ! ")

#question 4

answer=input("What does rom stands for ? ")
if answer=="read only memory":
    print("Correct !")
    score=score+1
else:
    print("Incorrect ! ")

#question 5

answer=input("What does os stands for ? ")
if answer=="operating system":
    print("Correct !")
    score=score+1
else:
    print("Incorrect ! ")


print("You got",score,"questions correct")
