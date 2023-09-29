##Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#  My name is Michele
#Then I would see the string:

# Michele is name My
#shown back to me.

def Reverse_sentence(string_input):
    list_of_Words=(string_input.split(" "))
    reversed_words = list_of_Words[::-1]
    reversed_string=" ".join(reversed_words)
    return reversed_string

if __name__=='__main__':
    sentence=input("Input you desired sentence you want to se reversed: ")
    print(Reverse_sentence(sentence))