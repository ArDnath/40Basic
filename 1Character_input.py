#Create a progaramme that asks the user to enter their neame and their age . Prrint out a message addressed to them that tells them the year that they will turn 100 years old .
name ,age = input("what is your name: "),int(input("what is your current age: "))

print(f"hi {name}")
century = 2023+(100-age)
print(f"youll turn 100 in year {century}")