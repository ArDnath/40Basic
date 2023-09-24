#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
import math
def divisors(n):
    divisor=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i ==0:
            divisor.append(i)
            if i != n // i:
                 divisor.append(n//i)
            
    divisor.sort()
    return divisor

if  __name__ == '__main__':
    no=int(input("Enter the number of whose you want to find out divisors of"))
    print(divisors(no))
    