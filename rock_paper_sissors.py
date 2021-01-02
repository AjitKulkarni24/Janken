import random

#create a list
l= ["Rock", "Paper", "Scissor"]

computer = l[random.randint(0, 2)]
player = True
while player==True:
    player = input('Rock, Paper, Scissors?')
    if player==computer:
        print('Tie!!') 
    elif player == "Rock":
        if computer == "Paper":
            
            print("you lose!, paper covers rock")
        else:
            print("you win!!, rock crushes scissors")    
        
    elif player == "Paper":
        if computer == "Scissors":
            print("you lose! Scissors cuts paper ")
        else:
            print("you win!! paper covers rock")
    
    
    elif player == "Scissors":
        if computer == "Rock":
            print("you lose! Rock crushes scissors")
        else:
            print("you win!! Scissors cuts paper ")        

    else:
        print("invalid play!! Please check your spelling")