# input(): a function that prompts the user to enter data and return the entered data as string

name = input("Enter your name: ")
age  = int(input("Enter your age: "))

print(f"Hello {name.capitalize()}!")
print(f"I am {age} years old!")