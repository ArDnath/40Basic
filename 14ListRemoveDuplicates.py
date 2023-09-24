#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def setRemoveDuplicates(lst):
    new_list=list(set(lst))
    return new_list
    
def loopRemove_duplicates(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
            
    return new_list
                
                
my_list = [1, 2, 2, 3, 4, 4, 5]
result = loopRemove_duplicates(my_list)
print(result)