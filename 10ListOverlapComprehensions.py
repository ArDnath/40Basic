import random

#Creating empty lists to call later
a = []
b = []
c = []

for i in range(0,20): #<-- Number of integers in list, in this case 20
    num = random.randint(1, 30) #<-- Inserting random digits
    a.append(num) #<-- Specifying in which list to insert inside of

for i in range(0,20):
    num = random.randint(1, 30)
    b.append(num)

for num in a: #<-- Assigning the variable 'num' as type 'integer'
    if num in b: #<-- Comparing numbers in list 'a' to list 'b'
        if num not in c: #<-- Verifying to remove duplicates
            c.append(num) #<-- Inserting into list 'c'

print(a) #This is to show the values in the 'a' list
print(b) #This is to show the values in the 'b' list
print(c) #Displays Common values