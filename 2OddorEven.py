#The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.


def even_or_odd(n):
    if n%2==0:
        print(f"{n} is an even number")
        
    elif n%4==0:
        print(f"{n} is a multiple of 4")
    else:
        print(f"({n}is an odd number")
        
def even_division(num,check):
    if num%check ==0:
        print(f"{num} is evenly divided by {check}")
    else:
        print(f"{num} is not evenly divided by {check}")
if __name__ == "__main__":
    number= int(input("Enter the number you want to check is even or odd"))
    even_or_odd(number)
    num=int(input("Enter a number"))
    check=int(input("Enter a number to check division"))
    even_division(num,check)
    
    