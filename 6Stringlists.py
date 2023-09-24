#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

def Palindrome(string):
    cleaned_string = string.replace(" ","").lower()
    
    rev_string = cleaned_string[::-1]
    return rev_string == cleaned_string


if __name__ == "__main__":
    string= input("input the word you want to check palindrome of: ")
    if Palindrome(string):
        print(f"{string} is a palindrome")
        
    else :
        print(f"{string} is not a palindrome")
    