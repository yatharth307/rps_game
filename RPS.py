# Importing the random module
import random

# initializing the variables
choices = ('r','p', 's')
cPoints = 0
pPoints = 0

def player():
    
    '''This fumc is used to get players choice.'''
    
    global choices  
    symbol = input("Choose either rock(r), paper(p), or scissors(s).").lower()
    
    if symbol not in choices:
        print("You did not enter a valid potion.")
        return player()  # use recursion to get a valid input
    else:
        return symbol  # if valid input return the answer
    
def computer():
    
    '''This function is used to get computers choice'''
    return random.choice(choices)

def game():
    
    '''This function is used to play a single round of game'''
    
    global cPoints, pPoints  # declaring both to be global
    pChoice = player()  # player choice
    cChoice = computer() # computer choice
    print("The computer has chosen", cChoice)
    print("You chose", pChoice)
    if pChoice == cChoice:  # checking for tie
        print("its a tie! No one gets a point. ")
    elif (pChoice == "r" and cChoice == "s") or (pChoice == "s" and cChoice == "p") or (pChoice == "p" and cChoice == "r"):  # checking if player scores a point
        
        print("You won! ")
        pPoints += 1  # increment the players point by 1
    else:  # checking if computer scores point
        print("Aww,  won. ")
        cPoints += 1  # increment the computer point by 1
    print()
    
print("Welcom to Rock Paper and Scissors game!!!")
while True:  # creating a infinite loop
    for i in range(5): # loop taht runs 5 times
        game()  # calling game 
    print("Good job!\nYour sccore is:", pPoints, "\nMy score is", cPoints)  # Displaying the result after 5 round 
    print()
    again = int(input("Press 1 to continue\nPress2 to reset and continue\npress3 to exit "))
    if again==1:  #this is executed if user wans to play another 5 rounds
        continue
    elif again==2:    # if the user wants to reset the scores and play another 5 round   
        pPoints=0
        cPoints=0
        continue
    else:  # this is for the user wants to quit
        break
print("Ok!  Bye!")
