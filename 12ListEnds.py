#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def first_last(list):
    new_list=[list[0],list[-1]]
    return new_list
print(first_last([5, 10, 15, 20, 25]))
    