#Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
def less_than5(list):
    new_list=[]
    for i in list:
        if i<5:
            new_list.append(i)
            
            
    return new_list
def input_list(n):
    #creating en empty list
    lst=[]
    
    #iterating till the range
    for i in range(n):
        ele=int(input(" "))
        lst.append(ele)
        
    return lst

def less_than_check(newlist,check):
    lst=[]
    for n in newlist:
        if n<check:
            lst.append(n)
            
    return lst            

        
            
if __name__ =="__main__":
    #number of elements as input
    n = int(input("Enter number of elements : "))
    list=input_list(n)
    print(less_than5(list))
    m = int(input("Enter numberof elements for an new list :"))
    newlist=input_list(m)
    check=int(input("Enter the number with which you would like to compare and see less than for in the new list:"))
    print(less_than_check(newlist,check))