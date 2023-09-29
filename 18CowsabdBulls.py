#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

def bullsAndCows():
   while True:
        attempts=0
        randomnum=str(random.randint(1000,9999))

        print(randomnum)
        guess=input("Guess the number you think it is")
        cows=0
        bulls=0
        if not guess.isdigit()or len(guess)!=4:
            print("{please enter a valid 4 digit number}")
        
        for i in range(4):
            if guess[i]== randomnum[i]:
                cows+=1
            
            elif guess[i] in randomnum:
                bulls+=1
            
            
        print(f"{cows} cow, {bulls} bull")
    
        attempts+=1
        if cows ==4:
            print(f"Congratualtions!!")
            break
    
    
if __name__ =="__main__":
    bullsAndCows()