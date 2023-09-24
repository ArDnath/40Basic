#Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
import math
def is_Prime(n):
    factor =0
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            factor+=1
            if i!=n//i:
                factor+=1
                
    return factor==2
if __name__=="__main__":
    number=int(input("Enter the number you want to check if is prime or not: "))
    if is_Prime(number):
        print(f"{number} is a prime number")
        
    else:
        print(f"{number} is not a prime number")