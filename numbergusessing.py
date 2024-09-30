import random 

top_of_range=input('Type a number: ')

if top_of_range.isdigit():
    top_of_range= int(top_of_range)

    if top_of_range <=0:
        print('Please type a number large than 0 next time. ')
        quit()

else:
    print("Please type a number next time")
    quit()

random_number= random.randint(0,top_of_range)
gusses = 0

while True:
    gusses +=1
    user_guess= input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time. ")
        continue
    
    if user_guess == random_number:
        print("You Got it!")
        break
    elif user_guess >random_number:
            print("your were above the number")
    else:
            print("you were below the number")
            
    

print(f"You got in {gusses} gussses")