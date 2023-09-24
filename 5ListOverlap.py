#Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random
length= int(input("input the length of the lists you want : "))
test2=[]
test1= []
for i in range(length):
    test1.append(int((random.random())*length))
    test2.append(int((random.random())*length))
print(test1, test2)
print(list(set(test1)&set(test2)))







