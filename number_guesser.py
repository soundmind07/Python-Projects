import random
top_of_range=input("Tyoe a number: ")

if top_of_range.isdigit():     #is digit returns true if all the characters are digit
    top_of_range=int(top_of_range)    #if our text contains only digits then we need to convert that text into a number

    if top_of_range<=0:
        print("Please type a number larger than 0 next time")
        quit()
else:
     print("Please type a number larger than 0 next time")
     quit()
     
random_number=random.randint(0,top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():    #is digit returns true if all the characters are digit
     user_guess=int(user_guess)    #if our text contains only digits then we need to convert that text into a number
    else:
        print("Please type a number larger than 0 next time")
        continue

    if user_guess==random_number:
        print("You got it ! ")
        break
    else:
        if user_guess>random_number:
            print("You were above the number! ")
        else:
            print("You were below the number! ")

print("You got it in", guesses,"guesses")


