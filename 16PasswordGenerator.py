#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
import string
import random

Uppercase=list(string.ascii_uppercase)
Lowercases =list(string.ascii_lowercase)
specialCharacters =list(string.punctuation)

length=int(input("Enter the length of your password: "))
password_list=[]
for i in range(length):
    if len(password_list)<length:
        password_list.append(random.choice(Uppercase))
        password_list.append(random.choice(Lowercases))
        password_list.append(random.choice(specialCharacters))
random.shuffle(password_list)
random_password="".join(password_list)
print(random_password)

#better optimized function for getting a stronger password everytime.

import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    length = int(input("Enter the length of your password: "))
    if length < 6:
        print("Password length should be at least 6 characters.")
        return
    random_password = generate_password(length)
    print("Generated Password:", random_password)

if __name__ == "__main__":
    main()
