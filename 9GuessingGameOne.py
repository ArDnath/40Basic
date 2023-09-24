import random
random_no= random.randint(1,9)
choice=int(input("Select a random number between 1 and 9 : "))
while True:
    if choice>random_no:
        print("you guess is higher than the no to be guessed")
    elif choice<random_no:
        print("your guess is lower the the number to be guessed")
        
    else:
        print("Yeepie!!this is the correct number")
        
    if input("Do you want to play again?(Y/N): ") =="N":
        break