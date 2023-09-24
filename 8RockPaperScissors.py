import random
#Make a computer vs playerRock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

choices =["Rock","Paper","Scissors"]


while True:
    user_move = input(f"what is your move from {choices} :").lower()
    
    comp_move=random.choice(choices).lower()
    
    if user_move == comp_move:
        print(f"It is a draw {user_move}s ")
        
    elif user_move== "rock":
        if comp_move=="paper":
            print("You win! Paper beats rock")
        else:
            print("You lose !! you win scissors beat rock")
    elif user_move== "scissors":
        if comp_move=="paper":
            print("You win! Scissors beats Paper")
            
        else:
            print("you lose!! you win Rock beats Scissors")
            
    elif user_move== "paper":
        if comp_move=="rock":
             print("You win!Paper beats Rock")
             
        else:
            print("You lose!! you win Rock beats")
     
    boolean=input("Do you want to keep on playing the game (y/n): ")
    if boolean=="n":
        break
    
    
    
           
    
    